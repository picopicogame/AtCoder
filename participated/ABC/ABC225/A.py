#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    s = list(input().rstrip())


    if s.count(s[0]) == 3:
        print(1)
    elif s.count(s[0]) == 2:
        print(3)
    elif s.count(s[1]) == 2:
        print(3)
    else:
        print(6)




if __name__ == "__main__":
    resolve()

