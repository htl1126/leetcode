# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def left_leave_sum(node):
            if node:
                if node.left and not node.left.left and not node.left.right:
                    self.ans += node.left.val
                map(left_leave_sum, (node.left, node.right))
        if root:
            left_leave_sum(root)
        return self.ans
