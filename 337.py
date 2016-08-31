# ref: https://discuss.leetcode.com/topic/39834/step-by-step-tackling-of-the
#              -problem


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_max(node):
            if not node:
                return 0, 0
            left_maxs = get_max(node.left)
            right_maxs = get_max(node.right)
            return (max(left_maxs) + max(right_maxs),
                    node.val + left_maxs[0] + right_maxs[0])
        return max(get_max(root))

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print sol.rob(root)
