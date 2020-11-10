# Ref: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274610/JavaC%2B%2BPython-Top-Down

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxAncestorDiff(self, root, max_val=0, min_val=100000):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxAncestorDiff(root.left, max(max_val, root.val), min(min_val, root.val)), \
            self.maxAncestorDiff(root.right, max(max_val, root.val), min(min_val, root.val)),) \
            if root else max_val - min_val

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(0)
    root.right.right.left = TreeNode(3)
    print sol.maxAncestorDiff(root)
