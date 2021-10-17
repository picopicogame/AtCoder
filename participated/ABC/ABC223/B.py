#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque
from copy import deepcopy
# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    str_list = list(input().rstrip())
    s_length = len(str_list)
    str_que = deque(str_list)
    ans_deque = deque()

    # 左シフトを文字数-1
    for i in range(s_length):
        left_s = str_que.popleft()
        str_que.append(left_s)
        temp_que = deepcopy(str_que)
        ans_deque.append(temp_que)



    print(*min(ans_deque), sep="")
    print(*max(ans_deque), sep="")


if __name__ == "__main__":
    resolve()

