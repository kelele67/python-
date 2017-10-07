
class Player(object):
    # __dict__, __weakref__
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

class Player2(object):
    __solts__ = ['uid', 'name', 'status', 'level']
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level
