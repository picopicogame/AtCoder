#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, d, h = map(int, input().split())

    li_d = []
    li_h = []
    for i in range(n):
        di, hi = map(int, input().split())
        li_d.append(di)
        li_h.append(hi)


    # 傾きを求める
    min_s = 9999999
    min_i = 0
    for i in range(n):
        sl = (li_h[i] - h) / (li_d[i] - d)
        if sl < min_s:
            min_s = sl
            min_i = i

    # y切片を求める
    y0 = h - min_s * d
    #y0 = li_h[min_i] - ((li_h[min_i] - h) / (li_d[min_i] - d)) * li_d[min_i]
    if y0 <= 0:
        y0 = 0.0
    print(y0)

if __name__ == "__main__":
    resolve()
