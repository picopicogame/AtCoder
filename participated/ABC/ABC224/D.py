#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    m = int(input().rstrip())
    vertex_list = [tuple(map(int, input().split())) for _ in range(m)]

    pos_list = list(map(int, input().split()))

    graph_list = []

    print(vertex_list)


if __name__ == "__main__":
    resolve()

