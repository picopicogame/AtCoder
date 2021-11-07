#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from  decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    x = Decimal(input().rstrip())

    print(x.quantize(Decimal('0'), rounding= ROUND_HALF_UP))

    print(round(x,0)) # in 0.5 > out 0



if __name__ == "__main__":
    resolve()

