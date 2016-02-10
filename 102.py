# source: https://leetcode.com/discuss/83909/actually-simple-python-solution

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.level_dfs(root, 0, result)
        return result

    def level_dfs(self, node, level, result):
        if not node:
            return
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        self.level_dfs(node.left, level + 1, result)
        self.level_dfs(node.right, level + 1, result)

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print sol.levelOrder(root)
