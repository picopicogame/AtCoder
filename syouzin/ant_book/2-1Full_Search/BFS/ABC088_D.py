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

    distance = [[-1 for _ in range(w)] for _ in range(h)]

    # 白色の床を全て数える
    white_floor = 0
    for y in range(h):
        for x in range(w):
            if field[y][x] == ".":
                white_floor += 1
    # スタートとゴールは塗り替えられないので-2
    white_floor -= 2
    # スタートとゴール
    sx = 0
    sy = 0
    gx = w - 1
    gy = h - 1


    # 4方向ベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    pos_que = deque()
    pos_que.append((sx, sy))
    distance[sy][sx] = 0

    while pos_que:
        x, y = pos_que.popleft()

        # ゴール地点
        if x == gx and y == gy:
            break

        # 4方向へ移動
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 範囲内で黒の床でなければ進む
            if 0 <= nx < w and 0 <= ny < h and field[ny][nx] != "#" and distance[ny][nx] == -1:
                pos_que.append((nx, ny))
                distance[ny][nx] = distance[y][x] + 1

    if distance[gy][gx] == -1:
        print(-1)
        exit()
    print(white_floor - distance[gy][gx] + 1)


if __name__ == "__main__":
    resolve()
