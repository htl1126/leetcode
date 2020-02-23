# Def: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286725/JavaC%2B%2BPython-Revered-Inorder-Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        def traverse(node):
            if node:
                traverse(node.right)
                self.val += node.val
                node.val = self.val
                traverse(node.left)
        traverse(root)
        return root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    ans = sol.bstToGst(root)
    print ans.val, ans.left.val, ans.right.val
