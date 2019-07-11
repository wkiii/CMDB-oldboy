from conf import settings


class BasePlugin:
    def __init__(self):
        self.debug = settings.DEBUG
        self.path = settings.FILE_PATH

    def get_os(self, handler):
        # os = handler.cmd('uname')
        # if os == 'Linux':
        #     return os
        # else:
        #     return 'win32'
        return 'Linux'  # DEBUG 测试Linux系统

    def process(self, handler, hostname):
        os = self.get_os(handler)
        if os == 'win32':
            return self.win(handler, hostname)
        elif os == 'Linux':
            return self.linux(handler, hostname)

    def win(self, handler, hostname):
        raise NotImplementedError('win() must be Implement')

    def linux(self, handler, hostname):
        raise NotImplementedError('linux() must be Implement')
