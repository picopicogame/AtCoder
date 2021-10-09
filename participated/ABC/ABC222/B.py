#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, p = map(int, input().split())
    l_a = list(map(int, input().split()))

    ans = 0
    for score in l_a:
        if score < p:
           ans += 1

    print(ans)
if __name__ == "__main__":
    resolve()
