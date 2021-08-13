# ref: https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99926/Python-Inorder-Solution

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        def dfs(n):
            if n:
                dfs(n.left)
                vals.append(n.val)
                dfs(n.right)
        dfs(root)
        return min(abs(a - b) for a, b in zip(vals, vals[1:]))
