class Solution:
    def isUnivalTree(self, root: Optional[TreeNode], val=None) -> bool:
        if not root:
            return True
        if val is not None:
            return root.val == val and self.isUnivalTree(root.left, val) and self.isUnivalTree(root.right, val)
        return self.isUnivalTree(root.left, root.val) and self.isUnivalTree(root.right, root.val)
