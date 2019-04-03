#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表和元祖可以存储任意类型的对象
alist = [1,2,3,4,5]
print(alist)
print(alist[1])
print(alist[2:])
print(alist[:3])
alist[1] = 10
print(alist)

aTuple = ('robots',77,93,'try')
print(aTuple)
print(aTuple[:3])
aTuple[1] = 10  # 元组是只读的，不可修改

