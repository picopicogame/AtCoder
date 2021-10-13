#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

"""
    PyPyだとMLEでAC通らない。
    再帰はPythonで提出すべき
"""

def input():
    return sys.stdin.readline()


def resolve():
    h, w = map(int, input().split())
    # 2次元配列を作る
    field = [list(input().rstrip()) for i in range(h)]

    # スタート位置を探す
    start_flag = False
    for i in range(h):
        for j in range(w):
            if field[i][j] == "s":
                start_flag = True
                x = i
                y = j
                break

            if start_flag:
                break

    def dfs(x, y):

        # 今いるところを#に置き換える
        field[x][y] = "#"

        for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
                nx = x + dx
                ny = y + dy

                if (x == nx or y == ny) and not(x == nx and y == ny):
                    # nxとnyが範囲内か判定
                    if 0 <= nx < h and 0 <= ny < w:
                        if field[nx][ny] == "#":
                            continue
                        elif field[nx][ny] == "g":
                            print("Yes")
                            exit()
                        else:
                            dfs(nx, ny)
        return

    dfs(x, y)
    print("No")






if __name__ == "__main__":
    resolve()
