from conf import settings
from src.engine.agent import AgentHandler
from src.engine.ssh import SSHHandler
from src.engine.salt import SaltHandler
import importlib
from lib.import_class import import_module


def run():
    '''入口'''
    handler_string = settings.ENGINE_DICT.get(settings.ENGINE)
    cls = import_module(handler_string)
    obj = cls()
    obj.handler()
    print('资产采集')


















