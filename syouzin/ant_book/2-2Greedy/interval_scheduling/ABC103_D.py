#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    ab_list = []
    for i in range(m):
        a, b = map(int, input().split())
        ab_list.append([a, b])

    ab_list.sort()

    ans = 0

    pre_a = 0
    pre_b = 0

    for i, abpair in enumerate(ab_list):
        a, b = abpair
        if i == 0:
            pre_a = a
            pre_b = b
            ans += 1
            continue

        if pre_a <= a < pre_b:
            if pre_a < a:
                pre_a = a
            if pre_b > b:
                pre_b = b
            continue
        else:
            pre_a = a
            pre_b = b
            ans += 1

    print(ans)




if __name__ == "__main__":
    resolve()
