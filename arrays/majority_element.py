"""
Majority Element
----------------
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than n // 2 times.
You may assume that the majority element always exists in the array.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Boyer-Moore voting algo
        count: int = 0
        candidate: int = -1 #place holder will always be overwritten on first iter of for loop
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1], 1),
        ([6, 5, 5], 5),
    ]

    for nums, expected in tests:
        result = solution.majorityElement(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
