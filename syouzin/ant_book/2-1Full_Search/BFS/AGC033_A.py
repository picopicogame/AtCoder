#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    h, w = map(int, input().split())
    field = [list(input().rstrip()) for _ in range(h)]

    # 4方向ベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    count = 0
    # タスクキュー
    total_que = deque()
    next_que = deque()
    for y in range(h):
        for x in range(w):
            if field[y][x] == "#":
                total_que.append((x, y))



    while True:

        if len(total_que) == 0:
            if len(next_que) == 0:
                break

            count += 1
            for i in range(len(next_que)):
                total_que.append(next_que.popleft())


        x, y = total_que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and field[ny][nx] != "#":
                next_que.append((nx, ny))
                field[ny][nx] = "#"

    print(count)

if __name__ == "__main__":
    resolve()
