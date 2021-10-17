#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    a_li = []
    b_li = []
    for i in range(n):
        a_item, b_item = map(int, input().split())
        a_li.append(a_item)
        b_li.append(b_item)

    all_second = 0

    sec_li = []
    for i in range(n):
        sec= a_li[i] / b_li[i]
        all_second += sec
        sec_li.append(sec)
    all_second /= 2.0

    final_sec = all_second
    for i in range(n):
        all_second -= sec_li[i]
        if all_second <= 0:
            final_index = i
            break
        else:
            final_sec = all_second

    ans = 0
    for i in range(final_index):
        ans += a_li[i]

    ans += b_li[final_index] * final_sec

    print(ans)



if __name__ == "__main__":
    resolve()

