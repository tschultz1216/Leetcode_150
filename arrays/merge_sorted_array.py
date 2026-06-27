"""
Merge Sorted Array
------------------
Merge nums2 into nums1 in-place. nums1 has m real elements followed by n zeros.
nums2 has n elements. Both are sorted in non-decreasing order.

Pattern: Two pointers — fill from the back to avoid overwriting real elements.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1: int = m -1
        pointer2: int = n - 1
        primaryPointer = m + n -1
        while pointer2 >= 0:
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[primaryPointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[primaryPointer] = nums2[pointer2]
                pointer2 -= 1
            primaryPointer -= 1


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]

    for nums1, m, nums2, n, expected in tests:
        solution.merge(nums1, m, nums2, n)
        status = "✅" if nums1 == expected else "❌"
        print(f"{status} Got: {nums1} | Expected: {expected}")
