#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()
    print(s.count('ZONe'))



if __name__ == "__main__":
    resolve()
