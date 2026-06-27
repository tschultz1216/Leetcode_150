"""
Best Time to Buy and Sell Stock
--------------------------------
Given an array prices where prices[i] is the currentPrice of a stock on day i,
return the maximum profit from a single buy/sell transaction where you must
buy before you sell. Return 0 if no profit is possible.
"""
from typing import Any, List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyPriceInt:int = prices[0]
        profit: int = 0
        for currentPrice in prices:
            if minBuyPriceInt > currentPrice:
                minBuyPriceInt = currentPrice
            todayProfit: int = currentPrice - minBuyPriceInt
            if todayProfit > profit:
                profit = todayProfit
        return profit


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([1], 0),
        ([2, 4, 1, 7], 6),
    ]

    for prices, expected in tests:
        result = solution.maxProfit(prices)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
