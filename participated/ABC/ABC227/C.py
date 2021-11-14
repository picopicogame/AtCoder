#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    max_a = math.ceil(math.pow(n, 1/3))
    max_b = math.ceil(math.pow(n, 1/2))
    #print(max_a,max_b)
    ans = 0
    ans2 = 0
    for a in range(1,max_a+1):
        temp = n//a
        for b in range(a,max_b+1):
            """
            for c in range(1, n+1):
                if b > c:
                    continue
                if a*b*c <= n:
                    ans += 1
            """
            if a*b*b > n:
                break
            ans2 += temp//b - (b-1)

    print(int(ans2))




if __name__ == "__main__":
    resolve()

