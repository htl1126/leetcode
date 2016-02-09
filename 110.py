# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_height(root):
            if not root:
                return 0
            else:
                l, r = get_height(root.left), get_height(root.right)
            if l != None and r != None and abs(l - r) <= 1:
                return 1 + max(l, r)
            else:
                return None
        return get_height(root) != None

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    #root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print sol.isBalanced(root)
