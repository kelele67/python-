# -*- coding: utf-8 -*- 
#!/bin/python
import sys
import os

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************

  
import itertools  
  
def GenAllExpr(card_4, ops_iter):  
    allexpr = []  
    try:  
        while True :  
            l = list(ops_iter.next()) + card_4  
            its = itertools.permutations(l, len(l))  
            try :  
                while True :  
                    yield its.next()  
            except StopIteration :  
                pass  
    except StopIteration:  
        pass  
  
def CalcRes(expr):  
    opmap = {'+':lambda a,b:a+b, '-':lambda a,b:a-b, '*':lambda a,b:a*b,   
            '/':lambda a,b:a/(b+0.0)}  
    expr_stack = []  
    while expr:  
        t = expr.pop(0)  
        if type(t) == float : expr_stack.append(t)  
        else :  
            if len(expr_stack) < 2 : return False  
            else :  
                a = expr_stack.pop()  
                b = expr_stack.pop()   
                try:  
                    expr_stack.append(opmap[t](a,b))  
                except ZeroDivisionError:  
                    return False  
    return expr_stack[0]  
  
  
def Check24(cards, n): 
    result = []
    for card in cards:
        ops = itertools.combinations_with_replacement('+-*/', n-1) #一个24点的计算公式可以表达成3个操作符的形式
        allexpr = GenAllExpr(card, ops) #数和操作符混合，得到所有可能序列 
        for expr in allexpr :
            res = CalcRes(list(expr))  
            if res and res == 24:   
                result.append("true")
                break
        else:
            result.append("false")
    return result

#******************************结束写代码******************************


_data_rows = 0
_data_cols = 0
_data_rows = int(raw_input())
_data_cols = int(raw_input())

_data = []
for _data_i in xrange(_data_rows):
    _data_temp = map(float,raw_input().strip().split(' '))
    _data.append(_data_temp)

  
res = Check24(_data, _data_cols)

for res_cur in res:
    print str(res_cur) + "\n"