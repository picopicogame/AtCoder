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

    distance = [[INF] * c for _ in range(r)]

    sx -= 1
    sy -= 1
    gx -= 1
    gy -= 1
    # 移動4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs():
        posx_que = deque()
        posy_que = deque()
        posx_que.append(sx)
        posy_que.append(sy)
        distance[sx][sy] = 0

        count = 0
        while posx_que:
            pos_x = posx_que.popleft()
            pos_y = posy_que.popleft()

            if pos_x == gx and pos_y == gy:
                break
            # 移動4方向
            for ii in range(4):
                #print(ii)
                nx = pos_x + dx[ii]
                ny = pos_y + dy[ii]
                #print("nx: " + str(nx))
                #print("ny: " + str(ny))
                #print(maze[nx][ny], distance[nx][ny])

                if 0 <= nx < c and 0 <= ny < r and maze[ny][nx] != "#" and distance[ny][nx] == INF:

                    posx_que.append(nx)
                    posy_que.append(ny)
                    #print(posx_que, posy_que)
                    distance[ny][nx] = distance[pos_y][pos_x] + 1
                    count += 1

        return distance[gy][gx]



    ans = bfs()
    print(ans)


if __name__ == "__main__":
    resolve()
