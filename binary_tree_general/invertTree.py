"""
226. Invert Binary Tree
----
Given the root of a binary tree, invert the tree, and return its root.

Inversion process:
  At every node, swap its left and right children, then recurse into both.
  Working bottom-up (post-order), each subtree is fully inverted before
  its parent swaps, so the entire mirror is built correctly in O(n) time
  with O(h) stack space where h is the height of the tree.

  Example:
       4                 4
      / \    --->       / \
     2   7             7   2
    / \ / \           / \ / \
   1  3 6  9         9  6 3  1

"""

from operator import invert
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # three cases, 
        # if left invert left. 
        # if right invert right.
        # if netiher swap left and right
        if root:
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
            swap = root.right
            otherSwap = root.left
            root.right = otherSwap
            root.left = swap
            return root


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


def level_order(root: Optional[TreeNode]) -> list:
    """Serialize a tree back to a level-order list for easy comparison."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # strip trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    solution = Solution()

    tests: list[tuple[list[Any], list[Any]]] = [
        # (input_values,          expected_level_order)
        ([4, 2, 7, 1, 3, 6, 9],  [4, 7, 2, 9, 6, 3, 1]),  # full example from problem
        ([2, 1, 3],               [2, 3, 1]),               # simple 3-node tree
        ([1],                     [1]),                     # single node
        ([],                      []),                      # empty tree
        ([1, 2, None, 3],         [1, None, 2, None, 3]),   # left-skewed input
    ]

    for input_vals, expected in tests:
        root = build_tree(input_vals) if input_vals else None
        result_root = solution.invertTree(root)
        result = level_order(result_root)
        status = "✅" if result == expected else "❌"
        print(f"{status} Got: {result} | Expected: {expected}")
