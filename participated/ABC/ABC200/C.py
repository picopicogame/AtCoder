#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import itertools
from collections import deque
from collections import defaultdict

def input():
    return sys.stdin.readline()


def resolve():
    n = input().rstrip()
    a = list(map(int, input().split()))

    ans = 0
    pre_dict = defaultdict(list)

    for i, ai in enumerate(a):
        amari = ai % 200
        pre_dict[amari].append(i)


    for i in range(200):
        li = pre_dict[i]
        len_li = len(li)
        # x*(x-1) /2通り
        ans += len_li * (len_li-1) / 2

    print(int(ans))



if __name__ == "__main__":
    resolve()
