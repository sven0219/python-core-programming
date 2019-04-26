#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

alphas = string.ascii_letters + '_'
nums = string.digits

print('Welcome to the Identifier Checker v1.0')
print('Testees must be at least 2char lopng.')

inp = input('Identifier to test?')

if len(inp) > 1:# 长度必须大于 1
    if inp[0] not  in alphas: # 判断第一个字母是不是字母或者下划线，若不是则打印提示并退出
        print("invalid: first symbol must be alphabetic")
    else:
        for otherChar in inp[1:]: #从第二个字母开始判断输入是否合法（数字、字母、下划线），不合法则打印提示并 break
            if otherChar not  in alphas + nums:
                print("invalid: remaining symbols must be alphanumeric")
                print("Erroe invaild:",otherChar)
                break
            else:
                print("okay as an identifier:",otherChar)
else:
    print("Length must be longer 2")