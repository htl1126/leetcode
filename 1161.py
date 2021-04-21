# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = [root]
        ans, lv_sum, lvl = 0, float('-inf'), 1
        while level:
            cur_sum = sum(n.val for n in level)
            if cur_sum > lv_sum:
                lv_sum = cur_sum
                ans = lvl
            new_level = [n for node in level for n in (node.left, node.right) if n]
            lvl += 1
            level = new_level
        return ans
