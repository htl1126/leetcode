# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root:
            ans, level = [], [root]
            while level:
                ans += [float(sum([v.val for v in level])) / len(level)]
                level = [n for node in level for n in (node.left,
                                                       node.right) if n]
            return ans
        return []

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.averageOfLevels(root)
