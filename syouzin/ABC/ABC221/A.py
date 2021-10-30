#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    a,b = map(int, input().split())

    if a == b:
        print("1")
        exit()
    print(32**(a-b))



if __name__ == "__main__":
    resolve()
