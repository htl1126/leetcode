# ref: https://discuss.leetcode.com/topic/36966/short-python-solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0, float('inf'), float('-inf')  # this line is important
            N1, n1, min1, max1 = dfs(node.left)
            N2, n2, min2, max2 = dfs(node.right)
            n = 1 + n1 + n2 if max1 < node.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, min2, node.val), max(max1, max2, node.val)
        return dfs(root)[0]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(7)
    print sol.largestBSTSubtree(root)
