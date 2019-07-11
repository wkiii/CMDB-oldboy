import importlib


def import_module(path_str):
    '''类的字符串  返回'''
    module_path, cls_str = path_str.rsplit('.', maxsplit=1)
    module = importlib.import_module(module_path)
    return getattr(module, cls_str)
