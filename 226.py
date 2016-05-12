# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.invert(root)

    def invert(self, node):
        if not node:
            return node
        if not node.left and not node.right:
            return node
        if node.left:
            node.left = self.invert(node.left)
        if node.right:
            node.right = self.invert(node.right)
        node.left, node.right = node.right, node.left
        return node

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root = sol.invertTree(root)
    print root.val
    print root.left.val
    print root.right.val
    print root.right.left.val
    print root.right.right.val
    print root.left.left.val
    print root.left.right.val
