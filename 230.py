# ref: https://leetcode.com/discuss/86469/python-easy-iterative-and
#              -recursive-solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.ans = None
        self.helper(root)
        return self.ans

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
            return
        self.helper(node.right)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(27)
    root.left = TreeNode(14)
    root.left.left = TreeNode(10)
    root.left.right = TreeNode(19)
    root.right = TreeNode(35)
    root.right.left = TreeNode(31)
    root.right.right = TreeNode(42)
    print sol.kthSmallest(root, 3)
