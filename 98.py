# source: https://leetcode.com/discuss/64051/clean-python-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
        if not root:
            return True
        return lower < root.val < upper and self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    print sol.isValidBST(root)
