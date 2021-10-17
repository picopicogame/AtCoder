#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    x = int(input().rstrip())

    if x < 100:
        print("No")
    elif x % 100 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    resolve()

