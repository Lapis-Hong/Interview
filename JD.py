#coding: utf-8
"""JD 2018 intern (2018京东实习生招聘的在线笔试)"""


# Prob 1:
# 将一个整数N分解成一个奇数X和一个偶数Y，若有多组解，输出Y最小的那组解，以空格分割，否则输出“No”
# 输入正整数列表nums (1 <= len(nums) <= 1000) ,其中每个正整数均不是2的幂次

# Solution:


def decompose(nums):
    for num in nums:
        if num % 2 == 0:
            y = 2
            while num/y % 2 == 0:
                 y *= 2
            print '%d %d' %(num/y, y)
        else:
            print 'No'


# Prob 2:
# 将一个字符串移除部分（0个或多个）字符使其变为回文串，空串不是回文串。
# 求所有可能的移除方案数（如果移除字符依次构成的序列不一样就是不同的方案）
# 输入一个字符串s，都是大写字母(1<=len(s)<=50), 输出可能数。
# 例子：
# 输入：ABA
# 输出： 5

# Solution:


def huiwen(string):
    count = 0
    def is_huiwen(string):
        if len(string) > 0:
            return string == string[::-1]
        else:
            return 0
    for i in range(2**len(string)):  # all possible sub sequence
        binary_num = bin(i)[2:][::-1]
        sub_seq = ''
        for ix, i in enumerate(binary_num):
            if i == '1':
                sub_seq += string[ix]
        if is_huiwen(sub_seq):
            count += 1
    print count


# Prob 3:
# 8x8的象棋谱，左下角坐标为（0，0）
# 求马走k步走到坐标（x, y）有多少种可能的路径。
# 例子：
# 输入：(3, 3)
# 输出：2

# Solution:
def ma():
    pass

if __name__ == "__main__":
    decompose((40, 23, 18))
    huiwen('ABA')
