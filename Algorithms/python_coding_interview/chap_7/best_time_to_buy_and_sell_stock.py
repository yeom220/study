# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
import sys
from typing import List

prices = [7, 1, 5, 3, 6, 4]
expected = 5


def maxProfit(self, prices: List[int]) -> int:
    # 1.브루트 포스로 계산
    # max_price = 0
    # for i in range(0, len(prices)):
    #     for j in range(i, len(prices)):
    #         max_price = max(prices[j] - prices[i], max_price)
    # return max_price

    # 2.저점과 현재 값과의 차이 계산
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(price - min_price, profit)
    return profit


output = maxProfit(prices, prices)
print(output == expected, output)
