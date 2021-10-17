#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    s_li = input().rstrip().split(sep=",")

    print(*s_li)


if __name__ == "__main__":
    resolve()
