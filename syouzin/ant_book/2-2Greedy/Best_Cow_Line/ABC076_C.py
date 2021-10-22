#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy
sys.setrecursionlimit(10**6)


def input():
    return sys.stdin.readline()


def resolve():
    s_dash = list(input().rstrip())
    t = list(input().rstrip())

    temp_s_dash = deepcopy(s_dash)
    temp_t = deepcopy(t)

    reverse_s_dash = [temp_s_dash.pop() for _ in range(len(temp_s_dash))]
    reverse_t = [temp_t.pop() for _ in range(len(temp_t))]



    exist_flag = False
    done_flag = False
    for i, s_char in enumerate(reverse_s_dash):
        break_flag = False
        if s_char == "?" or s_char == reverse_t[0]:

            for j, t_char in enumerate(reverse_t):
                if len(reverse_s_dash) > i+j and (reverse_s_dash[i+j] == t_char or reverse_s_dash[i+j] == "?" ):
                    if j == len(reverse_t) - 1:
                        done_flag = True
                else:
                    break_flag = True
                    break


        if break_flag:
            continue
        else:
            if done_flag:
                if exist_flag:
                    break
                count = i
                if len(reverse_s_dash) < count + len(reverse_t):
                    break
                for t_char in reverse_t:
                    reverse_s_dash[count] = t_char
                    count += 1
                exist_flag = True

    if not exist_flag:
        print("UNRESTORABLE")
        exit()

    for i, s_char in enumerate(reverse_s_dash):
        if s_char == "?":
            reverse_s_dash[i] = "a"

    reverse_s_dash.reverse()
    ans = ""
    for s in reverse_s_dash:
        ans += s

    print(ans)





if __name__ == "__main__":
    resolve()
