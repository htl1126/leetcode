# ref: https://discuss.leetcode.com/topic/15886/should-be-6-liner


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(first, last):
            trees = []
            for root in xrange(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
            return trees or [None]
        if not n:
            return []
        return generate(1, n)

if __name__ == '__main__':
    sol = Solution()
    sol.generateTrees(3)
