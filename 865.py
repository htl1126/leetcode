# Ref: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/discuss/146808/C%2B%2BJavaPython-One-Pass

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def deep(root):
            if not root:
                return 0, None
            l, r = deep(root.left), deep(root.right)
            if l[0] > r[0]:
                return l[0] + 1, l[1]
            if l[0] < r[0]:
                return r[0] + 1, r[1]
            return l[0] + 1, root
        return deep(root)[1]

if __name__ == "__main__":
    sol = Solution()
    print sol.subtreeWithAllDeepest(root)
