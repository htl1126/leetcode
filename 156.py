# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def flip_tree(node):
            if not node.left:
                return node, node
            new_root, new_rightmost = flip_tree(node.left)
            new_rightmost.left, new_rightmost.right, node.left, node.right = (
                node.right, node, None, None)
            return new_root, new_rightmost.right
        if root:
            root, _ = flip_tree(root)
        return root

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root = sol.upsideDownBinaryTree(root)
    print root.val, root.left.val, root.right.val
    print root.right.left.val, root.right.right.val
