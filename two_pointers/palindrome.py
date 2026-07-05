"""
palindrome
----
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
and numbers
Given a string s, return true if it is a palindrome, or false otherwise.

"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = re.sub(r"[^a-zA-Z0-9]", "", s)
        startIndex: int = 0
        endIndex: int = len(cleaned) - 1
        while startIndex < endIndex:
            if cleaned[startIndex] != cleaned[endIndex]:
                return False
            else:
                startIndex += 1
                endIndex -= 1
        return True

if __name__ == "__main__":
    solution = Solution()

    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
       ]

    for stringIn, expected in tests:
        result = solution.isPalindrome(stringIn)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
