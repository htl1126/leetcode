# ref: https://discuss.leetcode.com/topic/98426/c-python-straight-forward
#              -solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        level, s = [root], set()
        for node in level:
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                level += [node.left]
            if node.right:
                level += [node.right]
        return False

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    print sol.findTarget(root, 28)
