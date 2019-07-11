from api import models


def process_basic(info, server_list):
    # 更新主机资产信息 主机名不变
    # 修改主机信息
    basic_info = info['basic']['data']
    cpu_info = info['cpu']['data']
    main_board_info = info['main_board']['data']
    server_list.update(**basic_info, **cpu_info, **main_board_info)


def process_disk(info, server):
    disk_info = info['disk']['data']
    disk_query = models.Disk.objects.filter(server=server)
    disk_info_set = set(disk_info)
    disk_query_set = set(str(i.slot) for i in disk_query)

    # 新增
    add_slot_set = disk_info_set - disk_query_set
    add_disk_list = []
    for slot in add_slot_set:
        disk_info[slot]['server'] = server
        add_disk_list.append(models.Disk(**disk_info[slot]))
    if add_disk_list:
        models.Disk.objects.bulk_create(add_disk_list)

    # 更新
    update_slot_set = disk_info_set & disk_query_set
    for slot in update_slot_set:
        models.Disk.objects.filter(server=server, slot=slot).update(**disk_info[slot])

    # 删除
    del_slot_set = disk_query_set - disk_info_set
    if del_slot_set:
        models.Disk.objects.filter(server=server, slot__in=del_slot_set).delete()


def process_memory(info, server):
    memory_info = info['memory']['data']
    memory_query = models.Memory.objects.filter(server=server)
    memory_info_set = set(memory_info)
    memory_query_set = set(str(i.slot) for i in memory_query)

    # 新增
    add_slot_set = memory_info_set - memory_query_set
    add_memory_list = []
    for slot in add_slot_set:
        memory_info[slot]['server'] = server
        add_memory_list.append(models.Memory(**memory_info[slot]))
    if add_memory_list:
        models.Memory.objects.bulk_create(add_memory_list)

    # 更新
    update_slot_set = memory_info_set & memory_query_set
    for slot in update_slot_set:
        models.Memory.objects.filter(server=server, slot=slot).update(**memory_info[slot])

    # 删除
    del_slot_set = memory_query_set - memory_info_set
    if del_slot_set:
        models.Memory.objects.filter(server=server, slot__in=del_slot_set).delete()


def process_nic(info, server):
    nic_info = info['nic']['data']
    nic_query = models.NIC.objects.filter(server=server)
    nic_info_set = set(nic_info)
    nic_query_set = set(str(i.name) for i in nic_query)

    # 新增
    add_name_set = nic_info_set - nic_query_set
    add_nic_list = []
    for name in add_name_set:
        nic_info[name]['server'] = server
        add_nic_list.append(models.NIC(**nic_info[name]))
    if add_nic_list:
        models.NIC.objects.bulk_create(add_nic_list)

    # 更新
    update_name_set = nic_info_set & nic_query_set
    for name in update_name_set:
        models.NIC.objects.filter(server=server, name=name).update(**nic_info[name])

    # 删除
    del_name_set = nic_query_set - nic_info_set
    if del_name_set:
        models.NIC.objects.filter(server=server, name__in=del_name_set).delete()
