class Mat(object):
    """动态读，class 内部只存 temp 的值，每次取 pro 的时候实时计算"""
    def __init__(self, t):
        self.tmp = t

    @property
    def pro(self):
        return self.tmp * self.tmp

a = Mat(5)
print (a.tmp, a.pro)

a.tmp = 10
print (a.tmp, a.pro)

# 不加属性
# 5 <bound method Mat.pro of <__main__.Mat object at 0x1090144a8>>
# 10 <bound method Mat.pro of <__main__.Mat object at 0x1090144a8>>
# 加了之后
# 5 25
# 10 100

class Mat2(object):
    """两个都存，写入的时候两个都改"""
    def __init__(self, t):
        self.tmp = t

    @property
    def tmp(self):
        return self._tmp

    @tmp.setter
    def tmp(self, v):
        self._tmp = v
        self.pro = self.Pro(v)

    def Pro(self, t):
        return t * t

a = Mat2(5)
print (a.tmp, a.pro)
a.tmp = 10
print (a.tmp, a.pro)
# 5 25
# 10 100