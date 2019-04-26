#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 堆栈是一个后进先出的数据结构（LIFO)

# 定义
stack = []


# 存
def pushit():
    stack.append(input('Enter new String: ').strip())


# 删
def popit():
    if len(stack) == 0:
        print("Can't pop from in an empty stack!")
    else:
        print('Removed [', stack.pop(), ']')


# 查看
def viewstack():
    print(stack)


# 提示
def showmenu():
    prompt = """
    p(U)sh
    P(O)p
    (V)iew
    (Quit)
    
    Enter choice:
    """
    done = 0
    while not done:  # 死循环 打印菜单
        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked:[%s]' % choice)
            if choice not in 'uovq':
                print('invalid option,try again')
            else:
                chosen = 1
        if choice == 'q': done = 1
        if choice == 'u': pushit()
        if choice == 'o': popit()
        if choice == 'v': viewstack()


if __name__ == '__main__':
    showmenu()
