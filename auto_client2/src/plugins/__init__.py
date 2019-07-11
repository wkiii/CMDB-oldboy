from conf import settings
from lib.import_class import import_module


def get_server_info(handler, hostname=None):
    info = {}
    for i, path in settings.PLUGINS_DICT.items():
        cls = import_module(path)
        obj = cls()
        ret = obj.process(handler, hostname)
        info[i] = ret

    return info
