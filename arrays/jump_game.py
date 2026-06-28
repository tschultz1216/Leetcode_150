"""
Jump Game
---------
Given an integer array nums where nums[i] is the maximum jump length at position i,
return True if you can reach the last index starting from index 0, False otherwise.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach: int = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            furthestIndex: int = i + nums[i]
            max_reach = max(max_reach, furthestIndex)
        return True

if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0], True),
        ([0, 1], False),
        ([2, 0, 0], True),
    ]

    for nums, expected in tests:
        result = solution.canJump(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
