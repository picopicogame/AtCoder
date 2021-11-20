#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from bisect import bisect
# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n , k = map(int, input().split())
    p_li = [list(map(int, input().split())) for _ in range(n)]

    #print(p_li)

    res_li = []
    for i in range(n):
        res_li.append(sum(p_li[i]))

    #print(res_li)

    sorted_res = sorted(res_li, reverse=False)
    #print(sorted_res)


    for result in res_li:
        max_result = result + 300

        reversed_idx = bisect(sorted_res, max_result)
        idx = len(sorted_res) - reversed_idx +1

        if idx <= k:
            print("Yes")
        else:
            print("No")



if __name__ == "__main__":
    resolve()

