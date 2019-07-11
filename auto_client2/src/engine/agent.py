from .base import BaseHandler
from src.plugins import get_server_info
import requests
import json
import os
from conf import settings
from lib.security import gen_key, encrypt
import time


class AgentHandler(BaseHandler):

    def cmd(self, command):
        import subprocess
        ret = subprocess.getoutput(command)
        return ret

    def handler(self):
        # agent 下采集信息
        info = get_server_info(handler=self)
        # 根据主机名  判断 具体的操作
        if not os.path.exists(settings.CERT_PATH):
            # 文件不存在 新增
            info['type'] = 'create'
        else:
            # 更新
            with open(settings.CERT_PATH, 'r', encoding='utf-8') as f:
                old_hostname = f.read()
            hostname = info['basic']['data']['hostname']  # 最新主机名
            if old_hostname == hostname:
                # 更新资产
                info['type'] = 'update'
            else:
                info['type'] = 'update_hostname'
                info['old_hostname'] = old_hostname

        # 汇报 api
        now = time.time()
        response = requests.post(
            url=self.url,
            params={'key': gen_key(now), 'ctime': now},
            data=encrypt(json.dumps(info)),
            headers={'content-type': 'application/json'},
        )
        ret = response.json()

        if ret['status'] is True:
            with open(settings.CERT_PATH, 'w', encoding='utf-8') as f1:
                f1.write(ret['hostname'])
