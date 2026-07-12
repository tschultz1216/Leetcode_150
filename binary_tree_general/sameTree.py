"""
100. Same Tree
----
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


"""

from typing import Any, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def build_tree(values: list) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(val=values[0])
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

    tests: list[tuple[Any, Any, bool]] = [
        # (p_values, q_values, expected)
        ([1, 2, 3],         [1, 2, 3],         True),   # identical trees
        ([1, 2],            [1, None, 2],       False),  # same values, different structure
        ([1, 2, 1],         [1, 1, 2],          False),  # mirrored values
        (None,              None,               True),   # both empty
        ([1],               None,               False),  # one empty
        ([1, 2, 3, 4, 5],  [1, 2, 3, 4, 99],  False),  # deep leaf differs
        ([-1, -2, -3],      [-1, -2, -3],       True),   # negative values
    ]

    for p_vals, q_vals, expected in tests:
        p = build_tree(p_vals) if isinstance(p_vals, list) else p_vals
        q = build_tree(q_vals) if isinstance(q_vals, list) else q_vals
        result = solution.isSameTree(p, q)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
