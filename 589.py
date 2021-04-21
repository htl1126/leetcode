# Ref: https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/148867/Python-short-iterative-solution-beats-100-66-ms-faster-than-fastest-!
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend([child for child in reversed(node.children) if child])
        return ans
