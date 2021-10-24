#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from itertools import combinations

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    h, w = map(int, input().split())
    a_li = [list(map(int, input().split())) for _ in range(h)]

    h_index =[]
    for i in range(h):
        h_index.append(i)
    w_index = []
    for i in range(w):
        w_index.append(i)

    h_combi = itertools.combinations(h_index, 2)
    w_combi = itertools.combinations(w_index, 2)

    w_combi_list = list(w_combi)

    for h_c in h_combi:
        #print(h_c)
        for w_c in w_combi_list:
            #print(w_c, h_c)
            i1, i2 = h_c
            j1, j2 = w_c

            if a_li[i1][j1] + a_li[i2][j2] <= a_li[i2][j1] + a_li[i1][j2]:
                pass
            else:
                print("No")
                exit()

    print("Yes")



if __name__ == "__main__":
    resolve()

