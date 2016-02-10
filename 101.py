# source: https://leetcode.com/discuss/70107/python-56ms-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_symmetric_tree(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            elif p.val == q.val and check_symmetric_tree(p.left, q.right) and check_symmetric_tree(p.right, q.left):
                return True
            else:
                return False
        if root == None:
            return True
        else:
            return check_symmetric_tree(root.left, root.right)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    print sol.isSymmetric(root)
