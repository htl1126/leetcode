# ref: https://discuss.leetcode.com/topic/21287/python-short-recursive-solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_idx])
            root.left = self.buildTree(preorder, inorder[:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx + 1:])
            return root

if __name__ == '__main__':
    sol = Solution()
    tree = sol.buildTree([4, 2, 1, 3, 5], [1, 2, 3, 4, 5])
    print tree.val
    print tree.left.val
    print tree.right.val
    print tree.left.left.val
    print tree.left.right.val
