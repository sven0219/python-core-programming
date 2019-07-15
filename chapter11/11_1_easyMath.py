#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import random
import operator


ops = {'+': operator.add, '-': operator.sub}
MAXTRIES = 2


def doprob():
    op = random.choice('+-')
    nums = [random.randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d =' % (nums[0], op, nums[1])
    print(pr)
    oops = 0
    while True:
        try:
            if int(input()) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print ('answer : %s%s' % (pr, ans))
                break
            else:
                print ('incorrect... try again')
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print ('invalid input... try again')


def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y/n]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()