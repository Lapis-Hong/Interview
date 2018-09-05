# coding: utf-8
"""今日头条NLP实习面试

P1:
股票买卖的问题。给定一个数组代表股票每天的价格，请问在买卖一次的情况下，最大化净利润是多少？买卖多次呢？比如价格数组是{100,80,120,130,70,60,100,125}。

P2:
旋转序列[7,8,9,2,3,4,5]中找出某个值，要求复杂度O(lgn).
"""

def stock_transaction_single(prices):
    dp = [0] * len(prices)
    dp[1] = 0
    for i in range(2, len(prices)):
        dp[i] = max(prices[i]-min(prices[:i-1]), dp[i-1])
    return dp[-1]


def stock_transaction_multi(prices):
    profit = 0
    for i in range(0, len(prices)):
        if prices[i] < max(prices[i:]):
            profit += max(prices[i:]) - prices[i]
    return profit




def rotate_seq_search(arr, key):
    pass


if __name__ == '__main__':
    print(stock_transaction_single([100,80,120,130,70,60,100,125]))
    print(stock_transaction_multi([100,80,120,130,70,60,100,125]))

