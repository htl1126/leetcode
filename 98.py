# source: https://leetcode.com/discuss/64051/clean-python-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_valid_BST(node, upperbound=float('inf'), lowerbound=float('-inf')):
            if not node:
                return True
            if node.val >= upperbound or node.val <= lowerbound:
                return False
            return (check_valid_BST(node.left, min(upperbound, node.val), lowerbound)
                    and check_valid_BST(node.right, upperbound, max(node.val, lowerbound)))
        return check_valid_BST(root)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    print sol.isValidBST(root)
