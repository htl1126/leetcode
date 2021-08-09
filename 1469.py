class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(n):
            if n:
                if n.left and not n.right:
                    ans.append(n.left.val)
                if not n.left and n.right:
                    ans.append(n.right.val)
                dfs(n.left)
                dfs(n.right)
        dfs(root)
        return ans
