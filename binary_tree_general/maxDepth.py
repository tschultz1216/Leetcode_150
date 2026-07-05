"""
104. Maximum Depth of Binary Tree
----
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

"""

from typing import Any, Optional
import pandas as pd


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        countByOneOffset: int = 1
        if not root:
            return 0
        leftRoot = self.maxDepth(root.left)
        rightRoot = self.maxDepth(root.right)

        return countByOneOffset + max(leftRoot, rightRoot)
                    
            

# if __name__ == "__main__":
#     solution = Solution()

#     tests: list[tuple[list[Any],int]] = [
#         ([3,9,20,None,None,15,7], 3),
#         ([1,None,2], 2)
#        ]

#     for root, expected in tests:
#         result = solution.maxDepth(root)
#         status = "✅" if result == expected else "❌"
#         print(f"{status} Got: {result} | Expected: {expected}")
