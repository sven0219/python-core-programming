#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 python 不支持方法或函数重载
 type()内建函数可 以帮助你确认这一点。一个名字里究竟保存的是什么
"""

# python3 没有 long 类型
def displayNumTypeForIsinstance(num):
    print('num is',num)
    if isinstance(num, (int,  float, complex)):
        print('a number of type:', type(num).__name__)

    else:
        print
        'not a number at all!!'

displayNumTypeForIsinstance(-69)
displayNumTypeForIsinstance(9999999999999999999999)
displayNumTypeForIsinstance(98.6)
displayNumTypeForIsinstance(-5.2 + 1.9j)
displayNumTypeForIsinstance('xxx')


def displayNumType(num):
    print('num is',num)
    if type(num) == type(0):
        print ('an integer')
    elif type(num) == type(0.0):
        print ('a float')
    elif type(num) == type(0+0j):
        print ('a complex number')
    else:
        print ('not a number at all!!')



displayNumType(-69)
# displayNumType(9999999999999999999999)
displayNumType(98.6)
displayNumType(-5.2 + 1.9j)
displayNumType('xxx')
