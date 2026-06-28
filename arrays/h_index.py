"""
H-Index
-------
Given an array citations where citations[i] is the number of citations for
the ith paper, return the researcher's h-index — the maximum h such that
at least h papers have each been cited at least h times.
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        index: int = 0
        for citation in citations:
            if citation <= index:
                break  
            index += 1
        return index



if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([3, 0, 6, 1, 5], 3),
        ([1, 3, 1], 1),
        ([0], 0),
        ([100], 1),
        ([0, 0, 0], 0),
        ([4, 4, 4, 4], 4),
    ]

    for citations, expected in tests:
        result = solution.hIndex(citations)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
