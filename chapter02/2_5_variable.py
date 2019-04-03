#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 变量名命名规则：字母或者下划线开头，大小写敏感
# Python是动态语言类型，不需要预先声明变量的类型

counter = 0
name = 'Bob'
miles = 1000.0
counter = counter + 1
kilometers = 0.001 * miles
print("%f miles is the same as %f km" % (miles,kilometers))

# Python 不支持 C 语言中的自增 1 和自减 1 运算符， 这是因为 + 和 - 也是单目运算符， Python 会将 --n 解释为-(-n) 从而得到 n , 同样 ++n 的结果也是 n.