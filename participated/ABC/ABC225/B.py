#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    ab_li = []
    for i in range(n-1):
        a, b = map(int, input().split())
        ab_li.append([a, b])


    if ab_li[0][0] in ab_li[1]:
        star_vertex = ab_li[0][0]
    elif ab_li[0][1] in ab_li[1]:
        star_vertex = ab_li[0][1]
    else:
        print("No")
        exit()

    for i in range(2, n-1):
        if star_vertex not in ab_li[i]:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    resolve()

