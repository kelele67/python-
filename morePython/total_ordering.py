# -*- coding: utf-8 -*-

from functools import total_ordering
from abc import ABCMeta, abstractmethod

# 抽象基类
@total_ordering
class Shape(object):

    @abstractmethod
    def area(self):
        pass
    # 只用实现等于和小于
    def __eq__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() == obj.area()

    def __lt__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not Shape')
        return self.area() < obj.area()    

@total_ordering
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14
