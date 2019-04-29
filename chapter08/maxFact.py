#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if (num % count == 0):
            print ('largest factor of %d is %d' % (num, count))
            break
        count -= 1
    else:
        print (num, 'is prime')

for eachNum in range(1, 100):
    showMaxFactor(eachNum)

        