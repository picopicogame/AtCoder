#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n, q = map(int, input().split())

    front_deq = deque()
    back_deq = deque()
    ans_list = []

    for i in range(n+1):
        front_deq.append(0)
        back_deq.append(0)

    while q:
        q -= 1
        temp_li = list(map(int, input().split()))
        c = temp_li[0]
        x = temp_li[1]

        if len(temp_li) == 3:
            y = temp_li[2]

        if c == 1:
            back_deq[x] = y
            front_deq[y] = x
        elif c == 2:
            back_deq[x] = 0
            front_deq[y] = 0
        else:
            while front_deq[x] != 0:
                x = front_deq[x]

            ans = []
            while x != 0:
                ans.append(x)
                x = back_deq[x]

            ans_list.append(ans)

    for answer in ans_list:
        print(len(answer), *answer)





if __name__ == "__main__":
    resolve()

