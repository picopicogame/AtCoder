#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    weight = []
    for i in range(n):
        weight.append(int(input().rstrip()))

    box_list = []
    height = 0

    for i, w in enumerate(weight):
        if i == 0:
            box_list.append([w])
            height += 1

        for w_list in box_list:
            if w <= w_list[len(w_list)-1]:
                w_list.append(w)
                break
        else:
            box_list.append([w])
            height += 1

    print(height)

if __name__ == "__main__":
    resolve()
