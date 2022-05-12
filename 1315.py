# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode, parent_v=0) -> int:
        if not root:
            return 0
        s = self.sumEvenGrandparent(root.left, root.val) + self.sumEvenGrandparent(root.right, root.val)
        if parent_v and parent_v & 1 == 0:
            for n in (root.left, root.right):
                if n:
                    s += n.val
        return s
