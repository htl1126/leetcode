# ref: https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/148890/Python-3-lines-DFS-solution-w-a-very-simple-approach

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root
