# Ref: https://leetcode.com/problems/longest-univalue-path/discuss/108142/Python-Simple-to-Understand

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def search(node):
            if not node:
                return 0
            left_len, right_len = search(node.left), search(node.right)
            left = left_len + 1 if node.left and node.left.val == node.val else 0
            right = right_len + 1 if node.right and node.right.val == node.val else 0
            ans[0] = max(ans[0], left + right)
            return max(left, right)
        search(root)
        return ans[0]
