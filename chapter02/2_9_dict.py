#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字典是映射数据类型
# 由键值对组成，键和值都可以是任意数据类型

aDict = {'host': 'earth'} # create dict
aDict['port'] = 80 # add to dict
print(aDict)
print(aDict['host'])
for key in aDict:
    print(key,aDict[key])