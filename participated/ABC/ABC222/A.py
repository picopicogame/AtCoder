#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = input().rstrip()

    num = len(n)

    if num == 1:
        n = "000" + n
    elif num == 2:
        n = "00" + n
    elif num == 3:
        n = "0" + n


    print(n)




if __name__ == "__main__":
    resolve()
