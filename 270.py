# ref: https://leetcode.com/discuss/54438/4-7-lines-recursive-iterative-ruby
#              -c-java-python?show=65875


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        a = root.val
        child = root.left if target < a else root.right
        if not child:
            return a
        b = self.closestValue(child, target)
        return min((a, b), key=lambda x: abs(target - x))

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    print sol.closestValue(root, 3.0)
