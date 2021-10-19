#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    h, w, n = map(int, input().split())
    fixed_maze = [list(input().rstrip()) for _ in range(h)]
    fixed_distance = []
    inf = float('inf')
    # スタート地点
    for y in range(h):
        fixed_distance.append([])
        for x in range(w):
            if fixed_maze[y][x] == "S":
                sx = x
                sy = y
            fixed_distance[y].append(-1)

    maze = deepcopy(fixed_maze)
    distance = deepcopy(fixed_distance)

    distance[sy][sx] = 0
    # 4方向ベクトル
    dx = [1, 0, -1,  0]
    dy = [0, 1,  0, -1]

    # キュー
    posx_que = deque()
    posy_que = deque()
    posx_que.append(sx)
    posy_que.append(sy)

    # ネズミの体力
    rat_power = 1
    time_minute = 0
    while posx_que:

        x = posx_que.popleft()
        y = posy_que.popleft()

        # 現地点が食べられるチーズを生産する工場かどうか
        if maze[y][x] == str(rat_power):
            rat_power += 1
            # 経過時間を更新
            time_minute += distance[y][x]
            # 最短距離票を初期化
            distance = deepcopy(fixed_distance)
            distance[y][x] = 0
            # 目的地に着いたので今あるキューをクリア
            posx_que.clear()
            posy_que.clear()

        # チーズを食べ尽くしたか
        if rat_power > n:
            break

        # 4方向を探索
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 移動範囲で距離表で未到達なら実行する
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] != 'X' and distance[ny][nx] == -1:
                posx_que.append(nx)
                posy_que.append(ny)
                distance[ny][nx] = distance[y][x] + 1

    print(time_minute)

if __name__ == "__main__":
    resolve()
