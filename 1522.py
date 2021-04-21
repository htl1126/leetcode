# Ref: https://leetcode.com/problems/diameter-of-n-ary-tree/discuss/755068/Python3-recursion-O(n)-with-explanation-beat-98

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        ans = [0]
        def dfs(node):
            first, second = 0, 0
            for n in node.children:
                depth = dfs(n)
                if depth > first:
                    first, second = depth, first
                elif depth > second:
                    second = depth
            ans[0] = max(ans[0], first + second)
            return 1 + first
        dfs(root)
        return ans[0]
