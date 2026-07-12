"""
101. Symmetric Tree
----
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Symmetry check:
  A tree is symmetric if the left subtree is a mirror of the right subtree.
  Two subtrees are mirrors of each other when:
    1. Their root values are equal.
    2. The left child of one mirrors the right child of the other, and vice versa.

  Recurse with a helper that compares two nodes "from the outside in":
    isMirror(left, right)
      - both None        → True   (symmetric gap)
      - only one None    → False  (structural mismatch)
      - values differ    → False  (value mismatch)
      - otherwise        → isMirror(left.left, right.right)
                           and isMirror(left.right, right.left)

  Example — symmetric:          Example — not symmetric:
         1                              1
        / \                            / \
       2   2                          2   2
      / \ / \                          \   \
     3  4 4  3                          3   3

"""

from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.isMirror(root.left,root.right)
        else:
            return False

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isMirror(left=left.left, right=right.right) and self.isMirror(left=left.right, right=right.left)

def build_tree(values: list) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    solution = Solution()

    tests: list[tuple[list[Any], bool]] = [
        # (input_values,                   expected)
        ([1, 2, 2, 3, 4, 4, 3],           True),   # symmetric, two levels of children
        ([1, 2, 2, None, 3, None, 3],      False),  # same values, asymmetric structure
        ([1],                              True),   # single node is symmetric
        ([1, 2, 2],                        True),   # symmetric, no grandchildren
        ([1, 2, 3],                        False),  # root children differ
        ([1, 2, 2, 3, None, None, 3],      True),   # outer leaves match, inner gaps match
        ([1, 2, 2, None, 3, 3, None],      True),   # inner children match, outer gaps match
        ([1, 2, 2, None, 3, None, 3],      False),  # right-heavy vs left-heavy mismatch
    ]

    for input_vals, expected in tests:
        root = build_tree(input_vals) if input_vals else None
        result = solution.isSymmetric(root)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
