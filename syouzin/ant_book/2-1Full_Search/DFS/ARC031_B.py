#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()

def dfs(B_li, x, y):

    # 探索済みを海にする
    if B_li[x][y] == "o":
        B_li[x][y] = "x"

    # 4近傍を探索する
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 10 and 0 <= ny < 10:
                if (x == nx or y == ny) and not(x == nx and y == ny):
                    if B_li[nx][ny] == "o":
                        dfs(B_li, nx, ny)


def resolve():
    A_li = [list(input().rstrip()) for i in range(10)]

    # 埋め立てする
    for i in range(10):
        for j in range(10):
            if A_li[i][j] == "x":
                A_li[i][j] = "o"

                B_li = copy.deepcopy(A_li)
                dfs(B_li, i, j)

                one_island = True
                for ii in range(10):
                    for jj in range(10):
                        if "o" == B_li[ii][jj]:
                            one_island = False
                            break
                    if not one_island:
                        break

                if one_island:
                    print("YES")
                    exit()

                A_li[i][j] = "x"

    print("NO")


if __name__ == "__main__":
    resolve()
