"""
Two Sum II - Input Array Is Sorted
------------------------------------
Given a 1-indexed sorted array numbers, find two numbers that add up to target.
Return [index1, index2] (1-based). Exactly one solution exists. O(1) extra space required.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start: int = 0
        end: int = len(numbers)-1
        ## three cases, equal, less, or greater
        while(start<end):
            currentCheckValue:int = numbers[start] + numbers[end]
            if currentCheckValue == target:
                return[start+1,end+1]  
            if currentCheckValue < target:
                start += 1
            if currentCheckValue > target:
                end -= 1
        return[-1,-1]


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([5, 25, 75], 100, [2, 3]),
    ]

    for numbers, target, expected in tests:
        result = solution.twoSum(numbers, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
