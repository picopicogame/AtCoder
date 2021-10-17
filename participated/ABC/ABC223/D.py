#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

    full_graph = [[]]

    for i in range(m):
        for j in range(m):
            graph[i][j]


if __name__ == "__main__":
    resolve()

