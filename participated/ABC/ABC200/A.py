#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())

    if n % 100 == 0:
        ans = int(n / 100)
        print(ans)
        exit()
    else:
        ans = int(n / 100)
        ans += 1
        print(ans)


if __name__ == "__main__":
    resolve()
