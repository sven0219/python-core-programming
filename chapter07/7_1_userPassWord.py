#!/usr/bin/env python3
# -*- coding: utf-8 -*-

db = {}


def newuser():
    prompt = "Login desired:"
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


def olduser():
    name = input("login: ")
    pwd = input("password: ")
    passWord = db.get(name)
    if pwd == passWord:
        print("Welcome back,", name)
    else:
        print("Login incorrect!")


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: """

    done = 0
    while not done:
        chosen = 0
        while not chosen:
            try:
                choice = input(prompt)[0]
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print
            '\nYou picked: [%s]' % choice

            if choice not in 'neq':
                print("invalid menu option, try again")
            else:
                chosen = 1

        if choice == 'q': done = 1
        if choice == 'n': newuser()
        if choice == 'e': olduser()


if __name__ == '__main__':
    showmenu()
