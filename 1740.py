# Ref: https://leetcode.com/problems/find-distance-in-a-binary-tree/discuss/1039431/Python3-post-order-dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        ans = [0]
        def dfs(node):
            if not node:
                return False, float("-inf")
            l, l_h = dfs(node.left)
            r, r_h = dfs(node.right)
            
            if node.val in (p, q) or l and r:  # both p and q are in the subtree
                if l:
                    ans[0] += l_h + 1
                if r:
                    ans[0] += r_h + 1
                return True, 0
            return l or r, max(l_h, r_h) + 1  # pick the one without -inf height
        dfs(root)
        return ans[0]
