#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import deque

def input():
    return sys.stdin.readline()


def resolve():
    s = list(input().rstrip())

    s = deque(s)
    T = deque()
    r_flag = False
    for si in s:
        if si == 'R':
            if r_flag:
                r_flag = False
            else:
                r_flag = True
        else:
            if r_flag:
                if len(T) > 0 and T[0] == si:
                    T.popleft()
                else:
                    T.appendleft(si)
            else:
                if len(T) > 0 and T[-1] == si:
                    T.pop()
                else:
                    T.append(si)


    li_T = list(T)
    if r_flag:
        li_T.reverse()

    #print(''.join(li_T))
    str_t = ''.join(li_T)
    print(str_t)
    """
    str_t = ""
    for t in li_T:
        str_t += t

    print(str_t)
"""


if __name__ == "__main__":
    resolve()
