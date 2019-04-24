#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fname = input("Enter file name:")

print("attempt to open file %s for reading" % (fname))

try:
    fobj = open(fname,'r')
except IOError as e:
    print("*** file open error:",e)
else:
    for eachLine in fobj:
        print(eachLine)
    fobj.close()