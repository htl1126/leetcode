# ref: https://discuss.leetcode.com/topic/21286/python-short-solution
#              -recursively


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root

if __name__ == '__main__':
    sol = Solution()
    root = sol.buildTree([1, 3, 2], [3, 2, 1])
    print root.val
    print root.right.val
    print root.right.left.val
