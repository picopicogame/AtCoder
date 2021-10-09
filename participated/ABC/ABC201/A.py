#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    a_li = list(map(int, input().split()))

    a_li.sort()

    sub = a_li[1] - a_li[0]

    if sub == (a_li[2] - a_li[1]):
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    resolve()
