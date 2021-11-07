#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    t_li = []
    k_li = []
    a_li = [[] for _ in range(n)]

    temp_li = [list(map(int, input().split())) for _ in range(n)]

    for i, temp in enumerate(temp_li):
        for j, t in enumerate(temp):
            if j == 0:
                t_li.append(t)
            elif j == 1:
                k_li.append(t)
            else:
                a_li[i].append(t)


    task_set = set()

    def add_task(task_set, a_li, n):
        for task in a_li[n-1]:
            if task not in task_set:
                task_set.add(task)
                add_task(task_set, a_li, task)

    add_task(task_set, a_li, n)



    ans = t_li[n-1]

    for task in task_set:
        ans += t_li[task-1]

    print(ans)


if __name__ == "__main__":
    resolve()

