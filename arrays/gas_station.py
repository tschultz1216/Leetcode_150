"""
Gas Station
-----------
There are n gas stations on a circular route. gas[i] is the fuel available at
station i, cost[i] is the fuel needed to travel from station i to station i+1.
Starting with an empty tank, return the index of the station you can start from
to complete the circuit, or -1 if it is not possible. The solution is guaranteed
to be unique if it exists.
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        solution = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                solution = i + 1
                tank = 0
        return solution if total >= 0 else -1



if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
        ([1], [1], 0),
        ([1], [2], -1),
    ]

    for gas, cost, expected in tests:
        result = solution.canCompleteCircuit(gas, cost)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
