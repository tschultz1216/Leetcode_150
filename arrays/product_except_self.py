"""
Product of Array Except Self
-----------------------------
Given an integer array nums, return an array answer where answer[i] is the
product of all elements except nums[i]. Must run in O(n) time without division.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listLength: int = len(nums)
        left: list[int] = [1] * listLength
        runningFromLeft = 1
        for i in range(listLength):
            left[i] = runningFromLeft
            runningFromLeft *= nums[i]
        right: list[int] = [1] * listLength
        runningFromRight = 1
        for i in range(listLength - 1, -1 , -1):
            right[i] = runningFromRight
            runningFromRight *= nums[i]
        answer: list[int] = [left[i] * right[i] for i in range(listLength)]
        return answer


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-1, -1], [- 1, -1]),
    ]

    for nums, expected in tests:
        result = solution.productExceptSelf(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
