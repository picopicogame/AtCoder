#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
import copy

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    a_list = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    a_dic = {i: item for i, item in enumerate(a_list)}
    print(a_list)
    a_deque = deque(a_list)
    num_loop = int(n / 2)

    list_index = 0

    weight = 1
    divide = 1


    while a_deque:
        print(a_deque)
        multi = a_deque.popleft()
        print("multi: " + str(multi))
        if list_index != 0:
            list_index += 1

        while a_deque:
            if multi <= a_deque[0]:
                multi = a_deque.popleft()
                list_index += 1
            else:
                print("multi: " + str(multi) + "list_index: " + str(list_index))
                weight *= multi
                ans[list_index] = 1
                print(ans)
                break

        if len(a_deque) == 0:
            break

        divide = a_deque.popleft()
        print("divide: "+ str(divide))
        list_index += 1

        if len(a_deque) == 0:
            weight /= divide
            ans[list_index] = 1
            break

        while a_deque:
            if divide >= a_deque[0]:
                divide = a_deque.popleft()
                list_index += 1
            else:
                print("divide: " + str(divide) + "list_index: " + str(list_index))
                weight /= divide
                ans[list_index] = 1
                print(ans)
                break


        if len(a_deque) == 0:
            weight /= divide
            ans[list_index] = 1
            break




    """
    for i in range(num_loop):
        # 金
        gold = a_deque.pop()
        weight *= gold
        keys = [k for k, v in a_dic.items() if v == gold]
        for k in keys:
            if ans[k] == 0:
                ans[k] = 1
                break
        # 銀
        silver = a_deque.popleft()
        weight /= silver
        keys = [k for k, v in a_dic.items() if v == silver]
        for k in keys:
            if ans[k] == 0:
                ans[k] = 1
                break
    """
    print(*ans)


if __name__ == "__main__":
    resolve()

