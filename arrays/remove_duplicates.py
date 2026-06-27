"""
Remove Duplicates from Sorted Array
------------------------------------
Given an integer array nums sorted in non-decreasing order, remove duplicates
in-place so each unique element appears only once. The relative order must be
maintained. Return k, the number of unique elements, with nums[0..k-1] holding
those unique values in sorted order.
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index: int = 1
        for i in range(index,len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1], 1, [1]),
        ([1, 1], 1, [1]),
        ([1, 2], 2, [1, 2]),
    ]

    for nums, expected_k, expected_elements in tests:
        k = solution.removeDuplicates(nums)
        status = "✅" if k == expected_k and nums[:k] == expected_elements else "❌"
        print(f"{status} k={k} | First {k} elements: {nums[:k]} | Expected: {expected_elements}")
