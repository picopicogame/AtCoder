#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, k = map(int, input().split())

    for i in range(k):
        if n % 200 == 0:
            n = int(n / 200)
        else:
            n = n * 1000 + 200

    print(int(n))

if __name__ == "__main__":
    resolve()
