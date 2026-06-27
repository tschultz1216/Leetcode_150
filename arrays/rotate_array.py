"""
Rotate Array
------------
Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative. Must be done in-place.
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k: int = k % len(nums)
        split: int = len(nums) - k
        nums[:]= nums[split:] + nums[:split]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 3, [2, 1]),
        ([1], 0, [1]),
        ([1, 2, 3], 0, [1, 2, 3]),
    ]

    for nums, k, expected in tests:
        solution.rotate(nums, k)
        status = "✅" if nums == expected else "❌"
        print(f"{status} Got: {nums} | Expected: {expected}")
