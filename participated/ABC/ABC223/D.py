#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
import heapq

"""参考:https://atcoder.jp/contests/abc223/submissions/26660061"""

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b - 1].append(a - 1)

    for i in range(n):
        heapq.heapify(graph[i])

    key = [i for i in range(n)]

    graph_dic = dict(zip(key,graph))
    temp_que = deque()
    ans_li = []

    for j in range(n):
    #while temp_que:
        for i in graph_dic.keys():
            if len(graph_dic[i]) == 0:
                temp_que.append(i)
                break


        if len(temp_que) == 0:
            break

        pop_index = temp_que.popleft()
        ans_li.append(pop_index)
        graph_dic.pop(pop_index)

        for vertex_list in graph_dic:
            #if len(graph_dic[vertex_list]) == 0:
             #   continue
            #heapq.heappop(graph_dic[vertex_list])
            #print(graph_dic[vertex_list])

            graph_dic[vertex_list] = [s for s in graph_dic[vertex_list] if s !=pop_index ]





    if len(ans_li) != n:
        print("-1")
        exit()

    for i, ans in enumerate(ans_li):
        ans_li[i] += 1
    print(*ans_li)


if __name__ == "__main__":
    resolve()

