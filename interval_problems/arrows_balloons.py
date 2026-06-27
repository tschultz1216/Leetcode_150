"""
Minimum Number of Arrows to Burst Balloons
-------------------------------------------
Given a list of balloon intervals [xstart, xend], return the minimum number
of arrows needed to burst all balloons. An arrow at position x bursts any
balloon where xstart <= x <= xend.
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        result = 1
        points.sort(key=lambda x: x[0])
        arrowLimit: int = points[0][1]
        for start, end in points[1:]:
            if arrowLimit < start:
                result += 1
                arrowLimit = end
            else:
                arrowLimit= min(arrowLimit, end)
        return result


if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([[10,16],[2,8],[1,6],[7,12]], 2),
        ([[1,2],[3,4],[5,6],[7,8]], 4),
        ([[1,2],[2,3],[3,4],[4,5]], 2),
    ]

    for points, expected in tests:
        result = solution.findMinArrowShots(points)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {points}")
        print(f"   Expected: {expected} | Got: {result}\n")
