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
    query_li = [list(map(int, input().split())) for _ in range(q)]

    print(query_li)
    result_deque = deque()
    temp_deque = deque()
    for i in range(q):
        if query_li[i][0] == 1:
            print("test")
            q_n, x, y = query_li[i]
            temp_deque.append(x)
            temp_deque.append(y)
            for j, deq in enumerate(result_deque):
                first = deq[0]
                last = deq[-1]
                if first == y:
                    for k, deq2 in enumerate(result_deque):
                        last2 = deq2[-1]
                        if last2 == x:
                            result_deque[j].append(result_deque[k])
                            break
                    result_deque[j][0] = x
                    break
                elif last == x:
                    for k, deq2 in enumerate(result_deque):
                        first2 = deq2[0]
                        if first2 == y:
                            result_deque[j].append(result_deque[k])
                            break
                    result_deque[j][-1] = y
                    break

            result_deque.append(temp_deque)




    print(result_deque)

if __name__ == "__main__":
    resolve()

