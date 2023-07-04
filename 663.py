# Ref: https://leetcode.com/problems/equal-tree-partition/solutions/106724/two-pythons/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def tree_sum(node):
            if not node:
                return 0

            sums.append(node.val + tree_sum(node.left) + tree_sum(node.right))
            return sums[-1]
        
        sums = []
        tree_sum(root)
        return sums.pop() / 2 in sums
