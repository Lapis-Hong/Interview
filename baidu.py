#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/9/26

"""
题目一
宝箱怪
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
宝箱怪是游戏中常见的一种怪物，它们伪装成普通的宝箱，并在被玩家打开时攻击玩家。
假设你操控的游戏角色身处一个放着N个宝箱的房间，每个宝箱或者是普通的宝箱，或者是宝箱怪。每个宝箱上都贴着一张字条，字条上写着以下两种信息中的一种：
①第x个宝箱是普通宝箱；
②第x个宝箱是宝箱怪。

其中普通宝箱上的信息一定是真的，而宝箱怪上的信息可能是假的，
那么根据这些信息，有多少个宝箱一定是普通宝箱，又有多少个宝箱一定是宝箱怪？


题目二
超级变变变
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
魔法师小九有n个从左到右依次排成一行的魔法石，第i个魔法石的大小为Ai，Ai在[1, 10^9]的范围内。
同时使用排成一行的n个魔法石可以爆发出很大的威力，但是自己也会受到伤害，自损伤害数值为魔法石大小的逆序对个数，
逆序对是指满足i<j且Ai>Aj的 (i,j) 的对数（逆序对严格按照定义，如211，则逆序对为2个）。
魔法师小九希望减小伤害，他会选择且仅选择一块魔法石将其大小变成0，请问他最多可以将自损伤害数值降低到多少。

输入
第一行一个数n，表示魔法石的数量。（1≤n≤100000）
接下来一行n个数，第i个数表示Ai。（1≤Ai≤10^9）

输出
两个整数，用一个空格隔开，分别表示最小自损伤害数值和选择的魔法石序号，如果有多种最优选择方案，输出最小的魔法师序号（序号从1开始）。

样例输入
5
2 554 3 1
样例输出
5 2

Hint
样例解释
原逆序对数为7，将第二个魔法石变为0后，2 0 4 3 1共有5个逆序对。
"""


def inverse_pairs(arr):
    ans = 0
    n = len(arr)
    for i in xrange(n-1):
        for j in xrange(i+1, n):
            if arr[i] > arr[j]:
                ans += 1
    return ans


def min_inverse_pairs(arr):
    if len(arr) == 1:
        return 0, 1
    ans = inverse_pairs(arr)
    index = 0
    for i in xrange(len(arr)):
        arr_copy = arr[:]
        arr_copy[i] = 0
        cur_ans = inverse_pairs(arr_copy)
        if cur_ans < ans:
            ans = cur_ans
            index = i + 1
    return ans, index


def reduce_inverse_pairs(arr, index):
    n_increase_pairs = index
    n_decrease_pairs = 0
    for i in xrange(index+1, len(arr)):
        if arr[i] < arr[index]:
            n_decrease_pairs += 1
    return n_decrease_pairs - n_increase_pairs


def get_min_inverse_pairs(arr):
    n_pairs = inverse_pairs(arr)
    reduce_pairs = 0
    index = 0
    for i in xrange(len(arr)):
        cur_reduce_pairs = reduce_inverse_pairs(arr, i)
        if cur_reduce_pairs > reduce_pairs:
            reduce_pairs = cur_reduce_pairs
            index = i + 1
    return n_pairs-reduce_pairs, index


if __name__ == '__main__':
    # ans = inverse_pairs([3, 2, 1, 2])
    # print(ans)
    ans, idx = get_min_inverse_pairs([2, 5, 4, 3, 1])
    print(ans, idx)
