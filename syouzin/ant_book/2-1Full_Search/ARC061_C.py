#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def dfs(i, f, n, s):
    if i == (n-1):
        return eval(f)
    return dfs(i+1, f + s[i+1], n, s) + dfs(i+1, f + "+" + s[i+1], n , s)


def resolve():
    s = input().rstrip()
    n = len(s)
    ans = dfs(0, s[0], n, s)

    print(ans)




if __name__ == "__main__":
    resolve()
