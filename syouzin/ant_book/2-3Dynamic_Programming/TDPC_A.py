#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    p_li = list(map(int, input().split()))
    M = 100

    dp = [[0] * (n * M + 1) for _ in range(n+1)]
    print(p_li)




if __name__ == "__main__":
    resolve()
