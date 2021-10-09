#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    s_li = []
    t_li = []

    height_dic = {}
    for i in range(n):
        s, t = input().split()
        s_li.append(s)
        t_li.append(int(t))

    for i in range(n):
        height_dic[s_li[i]] = t_li[i]

    height_sorted = sorted(height_dic.items(), key=lambda x:x[1])

    name, height = height_sorted[-2]

    print(name)

if __name__ == "__main__":
    resolve()
