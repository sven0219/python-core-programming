#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
ls = os.linesep

import os

ls = os.linesep

# get filename
fname = input('Input the filename : ')
while True:

    if os.path.exists(fname):
        print
        "ERROR: '%s' already exists" % fname
        break
    else:
        print
        'OK, you create a new file now and its named %s' % fname
        # get file content (text) lines
        all = []
        print
        "\nEnter lines ('.' by itself to quit).\n"

        # loop until user terminates input
        while True:
            entry = input('> ')
            if entry == '.':
                break
            else:
                all.append(entry)

        # write lines to file with proper line-ending
        fobj = open(fname, 'w')
        fobj.writelines(['%s%s' % (x, ls) for x in all])
        fobj.close()
        print
        'DONE!'
        break
