# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        ans = [0]
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            cur_sum = node.val + left[1] + right[1]
            cur_avg = cur_sum / (left[0] + right[0] + 1)
            ans[0] = max(ans[0], cur_avg)
            return (left[0] + right[0] + 1, cur_sum)
        dfs(root)
        return ans[0]
