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
    n = int(input().rstrip())
    x_list = []
    y_list = []

    for i in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    def slope(x1, x2, y1, y2):
        return (y2-y1) / (x2-x1)

    index_list = []
    for i in range(n):
        index_list.append(i)

    tri_index = itertools.combinations(index_list, 3)

    count = 0
    for ind1, ind2, ind3 in tri_index:

        x1 = x_list[ind1]
        y1 = y_list[ind1]
        x2 = x_list[ind2]
        y2 = y_list[ind2]
        x3 = x_list[ind3]
        y3 = y_list[ind3]

        if x1 == x2 and x2 != x3:
            #print(ind1, ind2, ind3)
            count += 1
            continue
        if (y2-y1)*(x3-x1)-(x2-x1)*(y3-y1) != 0:
        #if y3 == slope(x1,x2,y1,y2)*x3 - slope(x1,x2,y1,y2) * x1 + y1:
            count += 1
            #print(ind1, ind2, ind3)

    print(count)
if __name__ == "__main__":
    resolve()

