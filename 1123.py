# Ref: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node:
                return 0, None
            h1, lca1 = helper(node.left)
            h2, lca2 = helper(node.right)
            if h1 > h2:
                return h1 + 1, lca1
            if h1 < h2:
                return h2 + 1, lca2
            return h1 + 1, node
        return helper(root)[1]

if __name__ == "__main__":
    sol = Solution()
    print sol.lcaDeepestLeaves(root)
