#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, k, a = map(int, input().split())

    amari = k % n

    ans = a - 1 + amari

    if ans > n:
        print(ans%n)
    elif ans == 0:
        print(ans+1)
    else:
        print(ans)

if __name__ == "__main__":
    resolve()

