#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 队列是一种先进先出(FIFO)的数据类型
queue = []


def enQ():
    queue.append(input('Enter new string :').strip())


def deQ():
    if len(queue) == 0:
        print('Can not pop from an enpty queue!')
    else:
        print('Removed [ ', queue.pop(0), ']')


def viewQ():
    print
    str(queue)


def showmenu():
    prompt = """
(E)nqueue
(D)nqueue
(V)iew
(Q)uit
Enter choice: """

    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (IndexError, EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'devq':
                print
                'invalid option, try again'
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'e': enQ()
        if choice == 'd': deQ()
        if choice == 'v': viewQ()


if __name__ == '__main__':
    showmenu()
