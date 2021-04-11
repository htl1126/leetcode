# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        level, ans = [root], root.val
        while level:
            new_level = [n for node in level for n in (node.left, node.right) if n]
            if new_level:
                ans = sum(n.val for n in new_level)
            level = new_level
        return ans
