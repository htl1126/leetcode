# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def get_children_sum(node):
            if node:
                l_sum = get_children_sum(node.left)
                r_sum = get_children_sum(node.right)
                if node.val == l_sum + r_sum:
                    ans[0] += 1
                return node.val + l_sum + r_sum
            return 0
        get_children_sum(root)
        return ans[0]
