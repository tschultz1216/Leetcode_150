"""
Remove Element
--------------
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The order of the elements may be changed. Return k, the
number of elements not equal to val, with those elements occupying nums[0..k-1].
"""
from typing import List


class Solution:
    ##O(n log n)
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        baseSize: int = len(nums)
        counter: int = 0
        negIter: int = baseSize - 1
        writePointer: int = baseSize - 1
        while negIter >= 0:
            if nums[negIter] == val:
                nums[negIter] = nums[writePointer]
                nums[writePointer] = -1
                counter += 1
                writePointer -= 1
            negIter -= 1
        return baseSize - counter
    
    ##O(n)
    def removeElementAlt(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index



if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([], 0, 0, []),
        ([1], 1, 0, []),
        ([1], 2, 1, [1]),
    ]

    for nums, val, expected_k, expected_elements in tests:
        k = solution.removeElementAlt(nums, val)
        result_elements = sorted(nums[:k])
        status = "✅" if k == expected_k and result_elements == sorted(expected_elements) else "❌"
        print(f"{status} k={k} | First {k} elements: {nums[:k]} | Expected: {expected_elements}")
