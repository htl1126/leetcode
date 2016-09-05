# ref: https://leetcode.com/discuss/86469/python-easy-iterative-and
#              -recursive-solution
# Take advantage of the property: inorder traversal forms a ordered list
# Counts at every inorder visit


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
        def find_kth(node):
            if not node:
                return
            find_kth(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            find_kth(node.right)
        self.k, self.ans = k, 0
        find_kth(root)
        return self.ans

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
