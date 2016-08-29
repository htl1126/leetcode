# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_num(node, num):
            if not node.left and not node.right:
                self.ans += int(num + str(node.val))
            else:
                if node.left:
                    get_num(node.left, num + str(node.val))
                if node.right:
                    get_num(node.right, num + str(node.val))
        if root:
            get_num(root, '')
        return self.ans

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(0)
    root.left = TreeNode(1)
    print sol.sumNumbers(root)
