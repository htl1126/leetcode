# Ref: https://leetcode.com/problems/complete-binary-tree-inserter/discuss/178424/C%2B%2BJavaPython-O(1)-Insert

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = [root]
        for n in self.tree:
            if n.left:
                self.tree.append(n.left)
            if n.right:
                self.tree.append(n.right)

    def insert(self, val: int) -> int:
        n = len(self.tree)
        self.tree.append(TreeNode(val))
        if n % 2:
            self.tree[(n - 1) // 2].left = self.tree[-1]
        else:
            self.tree[(n - 1) // 2].right = self.tree[-1]
        return self.tree[(n - 1) // 2].val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree[0]
