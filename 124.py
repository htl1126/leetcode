# ref: https://discuss.leetcode.com/topic/3767/python-question-on-class


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.maxsum = -2 ** 31

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_maxsum(node):
            if not node:
                return 0
            sum = node.val
            left_sum = get_maxsum(node.left)
            sum = sum + left_sum if left_sum > 0 else sum
            right_sum = get_maxsum(node.right)
            sum = sum + right_sum if right_sum > 0 else sum
            self.maxsum = max(self.maxsum, sum)
            return max(node.val, node.val + left_sum, node.val + right_sum)
        if root:
            get_maxsum(root)
        return self.maxsum

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print sol.maxPathSum(root)
