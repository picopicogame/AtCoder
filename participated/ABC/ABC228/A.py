#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    s, t, x = map(int, input().split())

    if s <= x <= t:
        print("Yes")
    elif (s > t) and (s <= x or x < t):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    resolve()

