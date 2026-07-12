"""
322. Coin Change
----
Given an integer array coins (infinite supply of each denomination) and a
target amount, return the fewest number of coins needed to reach exactly
that amount. Return -1 if it is not possible.

Approach — bottom-up DP (unbounded knapsack style):
  Build a 1-D table dp where dp[i] = minimum coins to make amount i.

  Initialisation:
    dp[0] = 0        (zero coins needed to make amount 0)
    dp[1..amount] = amount + 1   (sentinel "infinity" — never reachable with
                                  valid coins since max coins needed ≤ amount)

  Recurrence (for each amount i from 1 to amount):
    for each coin c in coins:
      if c <= i:
        dp[i] = min(dp[i], 1 + dp[i - c])

  Answer: dp[amount] if dp[amount] <= amount else -1

  Why it works:
    dp[i - c] is already the optimal answer for the sub-amount, and we
    add one coin (c) to complete it. Trying every coin and keeping the
    minimum guarantees optimality. Processing amounts in ascending order
    ensures dp[i - c] is already solved when we need it.

  Example — coins = [1, 5, 10, 25], amount = 36:
    dp[0]  = 0
    dp[1]  = 1   (1×1)
    dp[5]  = 1   (1×5)
    dp[10] = 1   (1×10)
    dp[11] = 2   (1×10 + 1×1)
    dp[25] = 1   (1×25)
    dp[36] = 3   (1×25 + 1×10 + 1×1)

  Time:  O(amount × len(coins))
  Space: O(amount)

"""

from typing import Any


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # bounded because the coin min value is 1 so amount is the upper solution limit
        UNREACHABLE = amount + 1
        # create dynamic programming tabulation for each 
        # tabulation of all numbers in range of 1 to the amount passed into the function
        # and how many coins it takes to create that value
        
        dp = [UNREACHABLE] * UNREACHABLE
        # base case: 0 coins to make sub-amount 0
        dp[0] = 0  
        for subAmount in range(1, amount + 1):
            for coinValue in coins:
                if coinValue <= subAmount:
                    dp[subAmount] = min(
                        dp[subAmount],
                        1 + dp[subAmount - coinValue]
                    )
        if dp[amount] < UNREACHABLE:
          return dp[amount]
        else:
          return -1

if __name__ == "__main__":
    solution = Solution()

    tests: list[tuple[list[int], int, int]] = [
        # (coins,          amount,  expected)
        ([1, 5, 10, 25],   36,       3),   # 25 + 10 + 1
        ([1, 5, 10, 25],   30,       2),   # 25 + 5
        ([1, 2, 5],        11,       3),   # 5 + 5 + 1
        ([2],              3,       -1),   # impossible — only even sums reachable
        ([1],              0,        0),   # amount 0 needs 0 coins
        ([1],              1,        1),   # single coin exact match
        ([1],              2,        2),   # two pennies
        ([186, 419, 83, 408], 6249,  20),  # larger case
    ]

    for coins, amount, expected in tests:
        result = solution.coinChange(coins, amount)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected} | coins={coins} amount={amount}")
