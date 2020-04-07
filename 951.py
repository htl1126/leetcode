# Ref: https://leetcode.com/problems/flip-equivalent-binary-trees/discuss/200488/Python-straightforward-DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2:
            return root1 == root2
        if root1.left and root2.left and root1.left.val != root2.left.val or not root1.left and root2.left or root1.left and not root2.left:
            root1.left, root1.right = root1.right, root1.left
        return root1.val == root2.val and self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)

if __name__ == "__main__":
    sol = Solution()
    print sol.flipEquiv(root1, root2)
