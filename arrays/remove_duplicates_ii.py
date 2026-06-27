"""
Remove Duplicates from Sorted Array II
---------------------------------------
Given an integer array nums sorted in non-decreasing order, remove duplicates
in-place such that each unique element appears at most twice. Return k, the
number of elements remaining, with nums[0..k-1] holding the final result in
sorted order. O(1) extra memory required.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        index = 2
        for i in range(index, len(nums)):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
        ([1], 1, [1]),
        ([1, 1], 2, [1, 1]),
        ([1, 1, 1], 2, [1, 1]),
        ([1, 2, 3], 3, [1, 2, 3]),
    ]

    for nums, expected_k, expected_elements in tests:
        k = solution.removeDuplicates(nums)
        status = "✅" if k == expected_k and nums[:k] == expected_elements else "❌"
        print(f"{status} k={k} | First {k} elements: {nums[:k]} | Expected: {expected_elements}")
