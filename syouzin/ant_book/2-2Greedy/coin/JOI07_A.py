#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    price = int(input().rstrip())

    oturi = 1000 - price

    count = 0

    coin_list = [500, 100, 50, 10, 5, 1]

    for coin in coin_list:
        while oturi >= coin:
            count += 1
            oturi -= coin

    print(count)

if __name__ == "__main__":
    resolve()
