#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from collections import defaultdict

def input():
    return sys.stdin.readline()


def resolve():
    t, n = map(int, input().split())





    num_ans_dic = {}
    for j in range(1, 50):
        t_rate = (100+j) / 100
        pre_num = 0
        ans_list = {}
        for i in range(1,1000):
            num = int(t_rate * i)
            if pre_num == 0:
                pre_num = num
                continue
            elif (num-1) == pre_num:
                pre_num = num
            else:
                ans_list[i] = num -1
                pre_num = num

        num_ans_dic[j] = len(ans_list)

    print(num_ans_dic)

    t_rate = (100 + t) / 100

    kaisuu = num_ans_dic[t]

    temp = int(n / kaisuu)

    remain = n - temp*kaisuu

    nearly_price = temp*1000

    pre_num = 0
    print(remain, t_rate, nearly_price)
    count = 0
    for i in range(1,1000):
        num = int(t_rate * (i+nearly_price))
        if pre_num == 0:
            pre_num = num
            continue
        elif (num - 1) == pre_num:
            pre_num = num
        else:
            count += 1
            print(i+nearly_price, count , remain, num, pre_num)
            pre_num = num
            ans = num - 1
            if count == remain:
                break

    print(ans)

if __name__ == "__main__":
    resolve()
