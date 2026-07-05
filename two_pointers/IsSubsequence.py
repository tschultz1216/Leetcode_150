"""
392. Is Subsequence
----
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
import re

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        subsequence=0
        for i in range(0,len(t)):
            if subsequence <= len(s) -1:
                if s[subsequence] == t[i]:
                    subsequence += 1
        return subsequence == len(s)
                    
            

if __name__ == "__main__":
    solution = Solution()

    tests: list[tuple[str,str,bool]] = [
        ("abc","ahbgdc", True),
        ("axc","ahbgdc", False)
       ]

    for sIn, tIn, expected in tests:
        result = solution.isSubsequence(s=sIn,t=tIn)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
