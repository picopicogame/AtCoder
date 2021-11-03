#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    p_li = list(map(int, input().split()))
    M = 100

    # dp[i][j] i番目まで見てj点を取ることが可能か格納した配列
    dp = [[0] * (n * M + 1) for _ in range(n+1)]

    # 0点は必ずある
    dp[0][0] = 1

    for i, a in enumerate(p_li):
        for j in range(n * M +1):
            dp[i+1][j] = dp[i][j]
            if j >= a:
                dp[i+1][j] |= dp[i][j-a]

    print(sum(dp[n]))


if __name__ == "__main__":
    resolve()
