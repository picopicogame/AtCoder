#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    b = [list(map(int,input().split())) for _ in range(n)]


    if (b[0][0] % 7) + (m-1) > 7:
        print("No")
        exit()
    if (b[0][0] % 7) == 0 and m > 1:
        print("No")
        exit()

    pre = 0
    for i in range(n):
        if i == 0:
            pre = b[i][0]
            continue
        if (pre+7) != b[i][0]:
            print("No")
            exit()
        pre = b[i][0]

    for i in range(n):
        for j in range(m):
            if j == 0:
                continue

            if b[i][j-1]+1 != b[i][j]:
                print("No")
                exit()

    print("Yes")

if __name__ == "__main__":
    resolve()

