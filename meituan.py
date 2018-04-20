#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/20

"""美团2018春招

Prob1: 经典的gcd（最大公约数）

时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给你A数组，询问ΣΣA[gcd(i,j)],1<=i<=n,1<=j<=m

输入
每行有四个整数，N,n,m,p,其中N表示A数组长度,n,m,p为参数;对于A数组如下得出：

A[1]=p,A[x]=(A[x-1]+153)%p

数据范围
小数据 n,m<=N<=1000,p<=1000
大数据 n,m<=N<=100000,p<=100000

样例输入
10 1 2 10
样例输出
20 

Hint
输入样例2
10 2 2 10
输出样例2
33

样例解释
第一组样例生成的数组A为：10 3 6 9 2 5 8 1 4 7。最后输出的答案为：A[gcd(1,1)] + A[gcd(1,2)] = A[1] + A[1] = 20。
第二组样例生成的数组A为：10 3 6 9 2 5 8 1 4 7。最后输出的答案为：A[gcd(1,1)] + A[gcd(1,2)] + A[gcd(2,1)] + A[gcd(2,2)] = A[1] + A[1] + A[1] + A[2] = 33。


Prob2: 统计位数

时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
沫璃在探寻数学的奥秘，她现在想知道n以内的正整数一共有多少位数字。不统计前导零。

例如：n为13时，12345678910111213，共17位，则输出为17。

输入
第一行一个数T(T<=100)，表示数据组数。
对于每组数据，第一行1个整数n (1 <= n <= 10^9)

输出
对于每组数据，输出一行，表示数字位数和

样例输入
2
13
4
样例输出
17
4

Hint
n为13时，12345678910111213，共17位，则输出为17
"""
def gcm(a, b):
    assert a > 0 and b > 0,'parameters must be greater than 0.'
    if a >= b:
        if a % b == 0:
            return b
        else:
            return gcm(b, a - b)
    else:
        return gcm(b, a)

def gcd(x, y):
    smaller = y if x > y else x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            res = i
    return res


def prob1(N, m, n, p):
    res = 0
    arr = []
    arr.append(p)
    for i in range(1, N):
        arr.append((arr[i - 1] + 153) % p)

    for i in range(1, m + 1):
        for j in range(i + 1, n + 1):
            res += 2 * arr[gcd(i, j) - 1]
    for i in range(1, m + 1):
        res += arr[gcd(i, i) - 1]
    print res


def prob2(n):
    res = 0
    for i in range(0, len(str(n))-1):
        res += (i+1) * 9 * 10 ** i
    res += len(str(n)) * (n - 10**(len(str(n))-1) + 1)
    print res

if __name__ == '__main__':
    # N, n, m, p = map(int, raw_input().split())
    prob1(10, 2, 2, 10)
    prob2(123)