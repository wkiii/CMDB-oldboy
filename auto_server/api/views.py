from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import JsonResponse

#
# @csrf_exempt
# def asset(request):
#     if request.method == 'GET':
#         return JsonResponse(['c{}.com'.format(i) for i in range(1, 101)], safe=False)
#     data = json.loads(request.body.decode('utf-8'))
#     return HttpResponse('ok')


from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api.service import process_basic, process_disk, process_memory, process_nic
import time
from utils.security import gen_key, decrypt
from django.http.response import HttpResponse


TOKEN_HISTORY = {}


class AuthView(APIView):

    def dispatch(self, request, *args, **kwargs):
        key = request.GET.get('key')
        ctime = request.GET.get('ctime')

        now = time.time()
        if now - float(ctime) > 1:
            return HttpResponse({'status': 3, 'msg': '超时'})

        if key in TOKEN_HISTORY:
            return HttpResponse({'status': 2, 'msg': 'key已初占用'})

        if key != gen_key(ctime):
            return HttpResponse({'status': 1, 'msg': '验证失败'})

        TOKEN_HISTORY[key] = None
        ret = super().dispatch(request, *args, **kwargs)
        return ret


class Text(APIView):
    def post(self, request):
        return Response({'status': 0, 'msg': ''})


class Asset(AuthView):
    def get(self, request):
        # return JsonResponse(['ww{}.com'.format(i) for i in range(1, 2)], safe=False)
        return Response(['ww{}.com'.format(i) for i in range(1, 100)])

    def post(self, request):
        # info = request.data
        date = decrypt(request.body)
        info = json.loads(date.decode('utf-8'))
        active_type = info.get('type')

        if active_type == 'create':
            # 新增主机
            basic_info = info['basic']['data']
            cpu = info['cpu']['data']
            main_board = info['main_board']['data']
            server_obj = models.Server.objects.create(**basic_info, **cpu, **main_board)

            # 添加硬盘信息
            disk_info = info['disk']['data']
            disk_list = []
            for disk in disk_info.values():
                disk_list.append(models.Disk(**disk, server=server_obj))
            models.Disk.objects.bulk_create(disk_list)

            # 添加网卡信息
            nic_info = info['nic']['data']
            nic_list = []
            for name, nic in nic_info.items():
                nic_list.append(models.NIC(**nic, name=name, server=server_obj))
            models.NIC.objects.bulk_create(nic_list)

            # 添加内存信息
            memory_info = info['memory']['data']
            memory_list = []
            for memory in memory_info.values():
                memory_list.append(models.Memory(**memory, server=server_obj))
            models.Memory.objects.bulk_create(memory_list)

        elif active_type == 'update':
            hostname = info['basic']['data']['hostname']
            server_list = models.Server.objects.filter(hostname=hostname)
            server = server_list.first()
            process_basic(info, server_list)
            process_disk(info, server)
            process_memory(info, server)
            process_nic(info, server)

        elif active_type == 'update_hostname':
            # 更新主机资产信息 + 主机名
            old_hostname = info['old_hostname']
            hostname = info['basic']['data']['hostname']
            server_list = models.Server.objects.filter(hostname=old_hostname)
            server = server_list.first()
            server.hostname = hostname
            # server.save()

            process_basic(info, server_list)
            process_disk(info, server)
            process_memory(info, server)
            process_nic(info, server)

        ret = {'status': True, 'hostname': info['basic']['data']['hostname']}
        return Response(ret)
        # return HttpResponse('ok')
