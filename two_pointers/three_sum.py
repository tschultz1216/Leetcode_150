"""
3Sum
----
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #sort array
        #for each index
        #three pointers: start, next, end
        nums.sort()
        triplets = []

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            
            nextIndex = index + 1
            end = len(nums)-1

            while nextIndex < end:
                checkSum = nums[index] + nums[nextIndex] + nums[end]
                ## Three cases. Less than, equal too, or greater than

                if checkSum > 0:
                    end -= 1
                elif checkSum < 0:
                    nextIndex += 1
                else:
                    triplets.append([nums[index], nums[nextIndex], nums[end]])
                    nextIndex += 1
                    ## skip dupes
                    while nums[nextIndex] == nums[nextIndex-1] and nextIndex < end:
                        nextIndex += 1
        return triplets


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ]

    for nums, expected in tests:
        result = solution.threeSum(nums)
        result_sorted = sorted([sorted(t) for t in result])
        expected_sorted = sorted([sorted(t) for t in expected])
        status = "✅" if result_sorted == expected_sorted else "❌"
        print(f"{status} Got: {result_sorted} | Expected: {expected_sorted}")
