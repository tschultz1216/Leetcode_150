"""
Insert Interval
---------------
Given a sorted list of non-overlapping intervals and a new interval,
insert the new interval and merge any overlaps. Return the result.
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = False
        result: List[List[int]] = []
        for start, end in intervals:
            if end < newInterval[0]:
                result.append([start,end])
            elif start > newInterval[1]:
                if not inserted:
                    inserted = True
                    result.append(newInterval)
                result.append([start,end])
            else:
                newInterval = [min(newInterval[0], start),max(newInterval[1],end)]
        if not inserted:
            result.append(newInterval)
        return result

if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([[1,3],[6,9]], [2,5]),           # [[1,5],[6,9]]
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),  # [[1,2],[3,10],[12,16]]
    ]

    for intervals, newInterval in tests:
        print(f"Input:       {intervals}, newInterval={newInterval}")
        print(f"Output:      {solution.insert(intervals, newInterval)}\n")
