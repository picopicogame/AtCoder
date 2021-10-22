#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    a = list(input().rstrip())

    if len(a) >= 2:
        print("".join(a[:len(a)-1]))
    elif a[0] == "a":
        print("-1")
    elif len(a) == 1:
        print("a")





if __name__ == "__main__":
    resolve()
