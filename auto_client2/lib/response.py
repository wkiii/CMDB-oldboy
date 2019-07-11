class BaseResponse():
    def __init__(self):
        self.status = None
        self.error = False
        self.data = None

    @property
    def dict(self):
        return self.__dict__