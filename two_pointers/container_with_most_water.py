"""
Container With Most Water
--------------------------
Given an integer array height of length n, find two lines that together with
the x-axis form a container holding the most water. Return the maximum water.
Water = min(height[left], height[right]) * (right - left).
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer problem.
        # look at start and end
        # area is the product of min(pointer1,pointer2)*(pointer2-pointer1)
        left: int = 0
        right: int = len(height)-1
        maxArea:int = 0
        while left < right:
            distance:int = right-left
            minHeight:int = min(height[left],height[right])
            currentAre:int = minHeight * distance
            ## three cases. equal, greater, or less than
            maxArea = max(currentAre,maxArea)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea



if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 10, 5, 7, 8, 9], 36),
    ]

    for height, expected in tests:
        result = solution.maxArea(height)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
