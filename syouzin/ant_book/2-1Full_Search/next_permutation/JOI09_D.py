#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
import collections

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    k = int(input().rstrip())
    card_list = [int(input().rstrip()) for _ in range(n)]



    count = 0
    ans_set = set()
    for v in itertools.permutations(card_list, k):
        str_temp = ""
        for s in v:
            str_temp += str(s)

        ans_set.add(str_temp)

    print(len(ans_set))


if __name__ == "__main__":
    resolve()
