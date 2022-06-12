# Ref: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/discuss/107165/Python-Extremely-Easy-To-Understand-(Beats-91)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = [float('inf')]
        def dfs(node):
            if node:
                if root.val < node.val < ans[0]:
                    ans[0] = node.val
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return -1 if ans[0] == float('inf') else ans[0]
