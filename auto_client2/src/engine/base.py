from conf import settings
import requests
from concurrent.futures import ThreadPoolExecutor
from src.plugins import get_server_info
import json


class BaseHandler:

    def __init__(self):
        self.url = settings.ASSET_URL

    def cmd(self):
        raise NotImplementedError('cmd() must be Implement')

    def handler(self):
        raise NotImplementedError('handler() must be Implement')


class SSHandSaltHandler(BaseHandler):

    def handler(self):
        # 获取未采集的主机列表
        ret = requests.get(
            url=self.url
        )
        host_list = ret.json()
        print(host_list)
        pool = ThreadPoolExecutor(20)
        for hostname in host_list:
            pool.submit(self.task, hostname)

    def task(self, hostname):
        # 采集资产信息
        info = get_server_info(self, hostname)
        requests.post(
            url=self.url,
            data=json.dumps(info).encode('utf-8'),
            headers={'content-type': 'application/json'}
        )
