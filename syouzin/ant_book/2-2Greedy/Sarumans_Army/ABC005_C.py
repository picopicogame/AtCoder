#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    t = int(input().rstrip())
    n = int(input().rstrip())
    a_li = list(map(int,input().split()))
    m = int(input().rstrip())
    b_li = list(map(int,input().split()))

    make_total = 0
    wait_total = 0

    if len(a_li) < len(b_li):
        # 客のほうが多ければ自動的にno
        print("no")
        exit()
    else:
        max_size = len(a_li)

    pre_pos = 0
    for i in range(m):

        for j in range(pre_pos, n):
            if a_li[j] <= b_li[i] <= a_li[j] + t:
                pre_pos = j + 1
                break
        else:
            print("no")
            exit()

    print("yes")





if __name__ == "__main__":
    resolve()
