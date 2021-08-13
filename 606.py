class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        if root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
        if root.left:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        return str(root.val)
