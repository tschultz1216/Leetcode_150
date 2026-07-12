"""
559. Maximum Depth of N-ary Tree
----
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Nary-Tree input serialization uses level-order traversal where
each group of children is separated by None.

Approach — recursive DFS:
  maxDepth(root):
    - base case: root is None → return 0
    - recurse on every child, take the max child depth
    - return 1 + max(child depths)   (or 1 if no children)

  Example:
         1
       / | \
      3  2  4
     / \
    5   6
  → depth = 3  (1 → 3 → 5  or  1 → 3 → 6)

"""

from typing import Any, Optional


class Node:
    def __init__(self, val: int = 0, children: Optional[list] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depthMax = 1
        for child in root.children:
            depthMax = max(depthMax, self.maxDepth(child)+1)
        return depthMax


def build_nary_tree(values: list) -> Optional[Node]:
    """Build an N-ary tree from a level-order list where None separates child groups."""
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue = [root]
    i = 2                          # skip root and first None separator
    parent_idx = 0
    while i < len(values):
        children = []
        while i < len(values) and values[i] is not None:
            child = Node(values[i])
            children.append(child)
            queue.append(child)
            i += 1
        queue[parent_idx].children = children
        parent_idx += 1
        i += 1                     # skip the None separator
    return root


if __name__ == "__main__":
    solution = Solution()

    tests: list[tuple[list[Any], int]] = [
        # (level-order input with None separators,  expected depth)
        ([1, None, 3, 2, 4, None, 5, 6],   3),   # standard 3-level example
        ([1, None, 2],                      2),   # root with one child
        ([1],                               1),   # single node
        ([],                                0),   # empty tree
    ]

    for input_vals, expected in tests:
        root = build_nary_tree(input_vals) if input_vals else None
        result = solution.maxDepth(root)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
