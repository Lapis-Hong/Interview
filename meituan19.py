#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/9/6
import itertools

# n, k = 10, 2
# b = '1 0 0 1 1 1 1 0 1 0'
# strings = b.split(' ')

a = raw_input()
b = raw_input()

n, k = map(int, a.split(' '))
strings = b.split(' ')


def max_len(arr):
    max_res = 0
    res = 0
    for s in arr:
        if s == "1":
            res += 1
        else:
            if res > max_res:
                max_res = res
            res = 0
    return max_res


zero_idx = []
for idx, s in enumerate(strings):
    if s == '0':
        zero_idx.append(idx)

if k >= len(zero_idx):
    print(n)
else:
    max_res = 0
    all_set = itertools.permutations(zero_idx, k)
    for k_idx in all_set:
        strings_ = strings[:]
        for k in k_idx:
            strings_[k] = "1"
        # print(strings_)
        res = max_len(strings_)
        # print(res)
        if res > max_res:
            max_res = res
    print(max_res)
