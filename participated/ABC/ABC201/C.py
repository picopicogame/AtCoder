#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
import sys
from  itertools import combinations_with_replacement

def input():
    return sys.stdin.readline()


def resolve():
    s_li = list(input().rstrip())

    o = 0
    x = 0
    hatena = 0
    for s in s_li:
        if s == "o":
            o += 1
        elif s == "x":
            x += 1
        else:
            hatena += 1

    if o >= 5:
        print(0)
        exit()

    l = ['0', '1', '2']

    for i, v in  enumerate(itertools.combinations_with_replacement(l, 4)):
        print(i, v)

    h_list = itertools.product(l, repeat=4)

    for i, v in enumerate(h_list):
        print(i, v)

if __name__ == "__main__":
    resolve()
