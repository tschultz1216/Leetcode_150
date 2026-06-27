"""
Merge Intervals — LeetCode-style class solution
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged: List[List[int]] = [intervals[0]]
        
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start,end])
                
        return merged
                

if __name__ == "__main__":
    solution = Solution()

    tests = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],   # [[1,6],[8,10],[15,18]]
        [[1, 4], [4, 5]],                        # [[1,5]]
        [[4, 7], [1, 4]],                        # [[1,7]]
    ]

    for intervals in tests:
        print(f"Input:  {intervals}")
        print(f"Output: {solution.merge(intervals)}\n")
