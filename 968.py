# Ref: https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        # return values of dfs()
        # 0: a leaf
        # 1: parent of a leaf, so we install a camera
        # 2: this node has been covered
        def dfs(node):
            if not node:
                return 2
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                self.ans += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.ans
