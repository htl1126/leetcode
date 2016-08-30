# ref: https://discuss.leetcode.com/topic/17971/my-python-solution-in-o-lgn
#              -lgn-time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            return 2 ** right_depth + self.countNodes(root.left)

    def get_depth(self, node):
        if node:
            return 1 + self.get_depth(node.left)
        return 0

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    print sol.countNodes(root)
