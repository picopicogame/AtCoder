#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()

def search_vertex(graph:list, vertex_list):
    for vertex in vertex_list:
        if len(graph) == 1:
            break
        first = vertex[0] - 1
        second = vertex[1] - 1
        if graph[0] == first and graph[1] == second:
            graph.pop(0)
            search_vertex(graph, vertex_list)
        elif graph[1] == first and graph[0] == second:
            graph.pop(0)
            search_vertex(graph, vertex_list)

def resolve():
    n, m = map(int, input().split())
    vertex_list = [tuple(map(int, input().split())) for _ in range(m)]

    whole_list = [i for i in range(n)]

    graph_list = []

    for v in itertools.permutations(whole_list, n):
        if v[0] == 0:
            graph_list.append(list(v))

    ans = 0
    for graph in graph_list:
        search_vertex(graph, vertex_list)

        if len(graph) == 1:
            ans += 1

    print(ans)



if __name__ == "__main__":
    resolve()
