#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()

def dfs(s, i, ans):
    if i == 3:
        if eval(ans) == 7:
            return ans + "=7"
        return ans

    ans = dfs(s, i+1, ans + "+" + s[i+1])

    if ans[len(ans)-2:] == "=7":
        return ans
    ans = ans[:len(ans)-2]

    ans = dfs(s, i+1, ans + "-" + s[i+1])

    if ans[len(ans) - 2:] == "=7":
        return ans
    ans = ans[:len(ans) - 2]

    return ans


def resolve():
    s = input().rstrip()
    ans = ""
    ans = dfs(s, 0, s[0])
    print(ans)


if __name__ == "__main__":
    resolve()
