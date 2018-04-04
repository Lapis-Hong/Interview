#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lapis-hong
# @Date  : 2018/4/3

# 题目描述
# 输入一个字符串，输出该字符串中对称的子字符串的最大长度。比如输入字符串“12213”，由于该字符串里最长的对称子字符串是“1221”，因此输出4。
# 输入描述:
# 连续的字符串，字符串长度不会超过64，只包含数字和字母。
# 输出描述:
# 最长的对称字符串长度
# 示例1
# 输入
# 12321abc
# 输出
# 5
# 说明
# 最长对称字符串为“12321”，因此长度为5
def max_sym_substring(string):
    length = len(string)
    max_sym_len = 1
    for i in range(length-max_sym_len):
        for j in range(i+max_sym_len, length):
            substring = string[i:j+1]
            reverse_substring = substring[::-1]
            if substring == reverse_substring:
                sym_len = j+1-i
                if sym_len > max_sym_len:
                    max_sym_len = sym_len
    return max_sym_len

# 题目描述
# IPv6地址为128位，完整的文本格式写成8段16位的形式，例如：
# 2001:1002:FFFF:ABCD:1234:1234:0000:0001
#
# 简写时，会将其中全0的字段压缩，例如：
#
# 2001:0000:0000:0000:0000:0000:0000:0001会简写成2001::0001
#
# 0000:0000:0000:0000:0000:0000:0000:0001会简写成::0001或者::1
#
# IPv6地址包括以下类型：
#
# 地址类型
#
# 地址前缀（二进制）
#
# IPv6前缀标识
#
# 单播地址
#
# 未指定地址
#
# 00…0(128 bits)
#
# ::/128
#
# 环回地址
#
# 00…1(128 bits)
#
# ::1/128
#
# 链路本地地址
#
# 1111111010
#
# FE80::/10
#
# 站点本地地址
#
# 1111111011
#
# FEC0::/10
#
# 全球单播地址
#
# 其他形式
#
# -
#
# 组播地址
#
# 11111111
#
# FF00::/8
#
# 任播地址
#
# 从单播地址空间中进行分配，使用单播地址的格式
#
# 备注：地址标识中一般以”/”后带的数字来表示掩码，例如上面的”FF00::/8“表示的是前8比特为1，后面120比特为任意值
# 请实现一段代码，来判断输入的IPv6地址字符串的类型。
#
# 输入描述:
# 一行字符串，完整形式的IPv6地址
# 输出描述:
# 输出一个字符串，表示是何种类型的IPv6地址，输出可以是：
# Unspecified    未指定地址
# Loopback       环回地址
# LinkLocal       链路本地地址
# SiteLocal        站点本地地址
# GlobalUnicast     全球单播地址
# Multicast        组播地址
# Error              错误的地址，或者非完整形式IPv6地址的字符串
# 示例1
# 输入
# FE81:0001:0000:0000:FF01:0203:0405:0607
# 输出
# LinkLocal


def ipv6_address_classify(ipv6_address):
    ip_list = ipv6_address.split(':')
    if len(ip_list) != 8:
        print('Error')
    else:
        ip_string = ''.join(ip_list)
        if ip_string == '00000000000000000000000000000000':
            print('Unspecified')
        elif ip_string == '00000000000000000000000000000001':
            print('Loopback')
        elif ip_list[0] == 'FE80':
            print('LinkLocal')
        elif ip_list[0] == 'FEC0':
            print('SiteLocal')
        elif ip_list[0] == 'FF00':
            print('Multicast')
        else:
            print('GlobalUnicast')


import numpy as np

# 题目描述
# 华为应用市场举办安装应用奖励金币活动，不同的应用下载、试玩需要的流量大小不同，奖励的金币数量也不同，同一个应用多次下载只奖励一次金币，小华月末有一定的余量，计算下载哪些应用可以获取的金币最多？ 相同金币情况下，优先下排名靠前的应用。
#
# 输入描述:
# 输入分三行
# 第一行： 流量数，单位MB，整数，
# 第二行：应用排名顺序，下载、试玩需要流量数，单位MB，整数
# 第三行：应用奖励的金币数
# 输出描述:
# 输出应用列表：建议下载的应用顺序号，用一个空格分隔
# 示例1
# 输入
# 40
# 12 13 23 36
# 11 11 20 30
# 输出
# 1 3
# 说明
# 注意输出： 开头、末尾没有空格
# use greedy algo to calculate approximate solution
def download_app(inputs):
    download_list = []
    total_data, app_data, app_coin = inputs.split('\n')
    total_data = int(total_data)
    app_data = map(float, app_data.split(' '))
    app_coin = map(float, app_coin.split(' '))
    avg_coin = list(np.array(app_data) / np.array(app_coin))
    while True:
        if len(avg_coin) == 0:
            break
        avg_max = max(avg_coin)
        if avg_max > total_data:
            avg_coin.remove(avg_max)
        else:
            total_data -= app_data[avg_coin.index(avg_max)]
            if total_data > 0:
                download_list.append(avg_coin.index(avg_max)+1)
                avg_coin.remove(avg_max)
            else:
                break
    return ' '.join(map(str, download_list))

import sys

# use greedy algo to calculate approximate solution
total_data = int(sys.stdin.readline().strip())
app_data = map(float, sys.stdin.readline().strip().split(' '))
app_coin = map(float, sys.stdin.readline().strip().split(' '))
avg_coin = []
for i in range(len(app_data)):
    avg_coin.append(app_coin[i] / float(app_data[i]))

download_list = []

while True:
    if len(avg_coin) == 0:
        break
    avg_max = max(avg_coin)
    if avg_max > total_data:
        avg_coin.remove(avg_max)
    else:
        total_data -= app_data[avg_coin.index(avg_max)]
        if total_data > 0:
            download_list.append(avg_coin.index(avg_max)+1)
            avg_coin.remove(avg_max)
        else:
            break
download_list.sort()
print(' '.join(map(str, download_list)))

if __name__ == '__main__':
    n = max_sym_substring('abssddss')
    print(n)

    ipv6_address_classify('FE81:0001:0000:0000:FF01:0203:0405:0607')
    print(download_app('40\n12 13 23 36\n11 11 20 30'))


