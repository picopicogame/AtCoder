#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, x = map(int, input().split())
    A_li = list(map(int, input().split()))

    known_li = set()

    temp = A_li[x-1]
    known_li.add(x)
    if temp == x:
        print(1)
        exit()

    ans = 1
    while True:
        known_li.add(temp)
        temp = A_li[temp-1]
        ans += 1
        if temp in known_li:
            break



    print(ans)



if __name__ == "__main__":
    resolve()

