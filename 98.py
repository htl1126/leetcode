# source: https://leetcode.com/discuss/64051/clean-python-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root: TreeNode, minv=float('-inf'), maxv=float('inf')):
        if not root:
            return True
        if root.val >= maxv or root.val <= minv:
            return False
        return self.isValidBST(root.left, minv, min(maxv, root.val)) and
            self.isValidBST(root.right, min(maxv, root.val), maxv)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    print sol.isValidBST(root)
