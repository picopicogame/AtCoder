#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(r)]
    INF = float('inf')
    distance_temp = [INF] * c
    distance = []
    for i in range(r):
        distance.append(distance_temp)

    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs():
        posx_que = deque()
        posy_que = deque()
        posx_que.append(sx)
        posy_que.append(sy)
        distance[sx][sy] = 0
        print(sx, sy)
        print(distance[sx][sy])
        count = 0
        while posx_que:
            pos_x = posx_que.popleft()
            pos_y = posy_que.popleft()

            if pos_x == gx and pos_y == gy:
                break
            # 移動4方向
            for ii in range(4):
                nx = pos_x + dx[ii]
                ny = pos_y + dy[ii]
                if 0 <= nx < c and 0 <= ny < r and maze[nx][ny] != "#" and distance[nx][ny] == INF:
                    posx_que.append(nx)
                    posy_que.append(ny)
                    distance[nx][ny] = distance[pos_x][pos_y] + 1

            count += 1

        print(count)
        return distance[gx][gy]



    ans = bfs()
    print(ans)


if __name__ == "__main__":
    resolve()
