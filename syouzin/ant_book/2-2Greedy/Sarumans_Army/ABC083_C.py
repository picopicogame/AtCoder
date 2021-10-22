#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    x, y = map(int, input().split())

    ans = 0
    while x <= y:
        x *= 2
        ans += 1

    print(ans)


if __name__ == "__main__":
    resolve()
