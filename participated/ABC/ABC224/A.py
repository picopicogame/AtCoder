#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()
    if s[-2:] == "er":
        print("er")
    else:
        print("ist")


if __name__ == "__main__":
    resolve()

