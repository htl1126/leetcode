# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = [None]
        def dfs(node):
            if not node:
                return 0
            flag = 0
            if node.val == p.val:
                flag |= 2
            if node.val == q.val:
                flag |= 1
            flag |= dfs(node.left)
            flag |= dfs(node.right)
            if flag == 3 and not ans[0]:
                ans[0] = node
            return flag
        dfs(root)
        return ans[0]
