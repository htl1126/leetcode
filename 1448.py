# Ref: https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/635259/JavaC%2B%2BPython-One-line

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_v=-10000) -> int:
        return self.goodNodes(root.left, max(max_v, root.val)) + self.goodNodes(root.right, max(max_v, root.val)) + (root.val >= max_v) if root else 0
