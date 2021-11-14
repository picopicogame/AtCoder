#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    s_li = list(map(int, input().split()))

    for a in range(1, 150):
        for b in range(1, 150):
            area = 4*a*b + 3*a + 3*b
            if area in s_li:
                for _ in range(s_li.count(area)):
                    index = s_li.index(area)
                    s_li.pop(index)

    print(len(s_li))




if __name__ == "__main__":
    resolve()

