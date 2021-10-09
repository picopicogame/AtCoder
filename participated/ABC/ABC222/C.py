#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()

def make_rank_order(rank_dic,win_dic):
    sorted_rank = dict(sorted(win_dic.items(), key=lambda x:x[1], reverse=True))
    for cnt, i in enumerate(sorted_rank.keys()):
        rank_dic[cnt+1] = i
    return rank_dic


def janken_result(playerA_GCP, playerB_GCP):
    if playerA_GCP == playerB_GCP:
        return 0
    elif playerA_GCP == "G" and playerB_GCP == "C":
        return 1
    elif playerA_GCP == "C" and playerB_GCP == "P":
        return 1
    elif playerA_GCP == "P" and playerB_GCP == "G":
        return 1
    else:
        return 2

def janken(round, n, prs_list, win_dic, rank_dic):

    for i in range(n):
        j = i +1
        playerA = rank_dic[2*j-1]
        playerB = rank_dic[2*j]
        playerA_GCP = prs_list[playerA-1][round]
        playerB_GCP = prs_list[playerB-1][round]
        result = janken_result(playerA_GCP, playerB_GCP)
        if result == 1:
            win_dic[playerA] += 1
        elif result == 2:
            win_dic[playerB] += 1

    return prs_list, win_dic, rank_dic

def resolve():
    n, m = map(int, input().split())
    prs_list = []
    int_list = []
    for i in range(2*n):
        prs_list.append(input().rstrip())
        int_list.append(i+1)
    win_dic = {i: 0 for i in int_list}
    rank_dic = {i: i for i in int_list}

    for i in range(m):
        prs_list, win_dic, rank_dic = janken(i, n, prs_list, win_dic, rank_dic)
        rank_dic = make_rank_order(rank_dic, win_dic)

    for rank in rank_dic.items():
        print(rank[1])
if __name__ == "__main__":
    resolve()
