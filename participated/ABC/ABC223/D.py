#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
import heapq

"""参考:https://atcoder.jp/contests/abc223/submissions/26583631"""

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    indeg = [0 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        indeg[b] += 1 # 各頂点が入ってくる辺（入次数）をいくつ持っているか
        graph[a].append(b) # 隣接行列

    # 次数0の頂点を管理するheapキュー
    heap_list = []
    heapq.heapify(heap_list)

    # 各頂点に次数0の頂点を調べ、あればheapキューに入れる
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap_list, i)

    # 解答リスト
    ans_li = []

    # 幅優先探索
    while heap_list:
        i = heapq.heappop(heap_list)
        ans_li.append(i)
        for index in graph[i]:
            # 各頂点の入次数を減らす
            indeg[index] -= 1
            # 減らした結果、その頂点の入次数が0になるなら、heapキューに入れる
            if indeg[index] == 0:
                heapq.heappush(heap_list, index)

    # トポロジカルソートをしても入次数を持つ頂点があるなら解答なし
    if len(ans_li) != n:
        print("-1")
        exit()

    for i, ans in enumerate(ans_li):
        ans_li[i] += 1
    print(*ans_li)


if __name__ == "__main__":
    resolve()

