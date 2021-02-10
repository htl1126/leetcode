# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur_sum = [0]
        def visit(node: TreeNode):
            if not node:
                return
            visit(node.right)
            cur_sum[0] += node.val
            node.val = cur_sum[0]
            visit(node.left)
        visit(root)
        return root
