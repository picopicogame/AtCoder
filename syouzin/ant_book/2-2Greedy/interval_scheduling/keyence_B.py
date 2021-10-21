#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    x_li = []
    l_li = []
    pair_li = []
    for i in range(n):
        x, l = map(int, input().split())
        x_li.append(x)
        l_li.append(l)
        pair_li.append([x, l])

    pair_li.sort()


    arm_end_start = []
    arm_end = []

    for arm_x, arm_l in pair_li:
        arm_end_start.append([arm_x+arm_l,arm_x - arm_l])

    arm_end_start.sort()

    pre_end = -9999999999
    ans = 0

    for end, start in arm_end_start:

        if pre_end <= start:
            pre_end = end
            ans += 1

    print(ans)


if __name__ == "__main__":
    resolve()
