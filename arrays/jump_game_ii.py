"""
Jump Game II
------------
Given an integer array nums where nums[i] is the maximum jump length at index i,
return the minimum number of jumps to reach the last index. It is guaranteed
you can always reach the last index.
"""
from typing import Any, List


class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest:int = 0
        currentEnd:int = 0
        jumpCount:int = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, (i+nums[i]))
            if i == currentEnd:
                jumpCount += 1
                currentEnd = farthest
        return jumpCount


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([1, 2], 1),
        ([1, 1, 1, 1], 3),
    ]

    for nums, expected in tests:
        result = solution.jump(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
