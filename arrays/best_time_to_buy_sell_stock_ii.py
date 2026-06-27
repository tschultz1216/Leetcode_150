"""
Best Time to Buy and Sell Stock II
------------------------------------
Given an integer array prices where prices[i] is the price of a stock on day i,
return the maximum profit by buying and selling on multiple occasions. You may
not hold more than one share at a time, but you can sell and buy on the same day.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 1, 4], 3),
    ]

    for prices, expected in tests:
        result = solution.maxProfit(prices)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
