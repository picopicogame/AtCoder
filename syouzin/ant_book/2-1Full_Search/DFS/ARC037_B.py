#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    def dfs(now, prev):
        global tree_flag

        for i in tree[now]:
            if i != prev:
                if passed_memo[i]:
                    # すでに到達していたので閉路
                    tree_flag = False
                else:
                    passed_memo[i] = True
                    dfs(i, now)

    n, m = map(int, input().split())
    tree = [[] for i in range(n)]
    passed_memo = [False for i in range(n)]

    for i in range(m):
        ui, vi = map(int, input().split())
        tree[ui-1].append(vi-1)
        tree[vi-1].append(ui-1)


    ans = 0
    global tree_flag

    for i in range(n):
        if not passed_memo[i]:
            tree_flag = True
            dfs(i, -1)
            if tree_flag:
                ans += 1
            else:
                tree_flag = True

    print(ans)



if __name__ == "__main__":
    resolve()
