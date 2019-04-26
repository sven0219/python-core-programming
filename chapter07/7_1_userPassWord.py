#!/usr/bin/env python3
# -*- coding: utf-8 -*-

db = {}


def newuser():
    prompt = "Login desired!"
    while True:
        name = input(prompt)
        # Python 3.x不再支持 has_key() 函数，而被__contains(‘keyname’)所替代
        if db.__contains__(name):
            prompt = "name taken ,try another:!"
            continue
        else:
            break

        pwd = input("Password: ")
        db[name] = pwd


