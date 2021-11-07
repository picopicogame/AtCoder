#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    l_li = []
    temp_li = [list(map(int, input().split())) for _ in range(n)]
    temp_li.sort()
    #print(temp_li)
    a_li = [[] for _ in range(n)]
    for i, temp in enumerate(temp_li):
        for j, t in enumerate(temp):
            if j == 0:
                l_li.append(t)
            else:
                a_li[i].append(t)

    ans = 1
    for i , l in enumerate(l_li):
        if i == 0:
            continue

        if l != l_li[i-1]:
            ans += 1
            continue

        #print(a_li[i], a_li[i-1])
        if a_li[i] == a_li[i-1]:
            continue

        ans += 1

    print(ans)



if __name__ == "__main__":
    resolve()

