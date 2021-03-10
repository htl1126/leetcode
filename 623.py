# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(val=v, left=root)
            return new_root
        level, cur_d = [root], 1
        while level:
            if cur_d == d - 1:
                for node in level:
                    left, right = TreeNode(v, left=node.left), TreeNode(v, right=node.right)
                    node.left, node.right = left, right
                return root
            level = [n for node in level for n in (node.left, node.right) if n]
            cur_d += 1
