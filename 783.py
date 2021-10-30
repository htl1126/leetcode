# ref: https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/114834/C%2B%2BJavaPython-Inorder-Traversal-O(N)-time-Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = [float('-inf'), float('inf')] # pre and res
        def find(node):
            if node.left:
                find(node.left)
            vals[1] = min(vals[1], node.val - vals[0])
            vals[0] = node.val
            if node.right:
                find(node.right)
        find(root)
        return vals[1]
