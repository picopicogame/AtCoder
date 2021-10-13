#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()

def cook_meet(i, n, sum_time1, sum_time2, t_li, result_list:list):

    if i == n:
        if sum_time1 >= sum_time2:
            result_list.append(sum_time1)
        else:
            result_list.append(sum_time2)
        return

    cook_meet(i+1, n, sum_time1 + t_li[i], sum_time2, t_li, result_list)

    cook_meet(i+1, n, sum_time1, sum_time2 + t_li[i], t_li, result_list)


def resolve():
    n = int(input().rstrip())
    t_li = [int(input().rstrip()) for i in range(n)]

    res_list = []
    cook_meet(0, n, 0, 0, t_li, res_list)

    print(min(res_list))

if __name__ == "__main__":
    resolve()
