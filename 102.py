# source: https://leetcode.com/discuss/83909/actually-simple-python-solution


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS solution
class Solution(object):
    def levelOrder(self, root):
        res = []
        if root:
            level = [root]
            while level:
                res.append([n.val for n in level])
                level = [kid for node in level for kid in (node.left,
                                                           node.right) if kid]
        return res


# DFS solution
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)
        def dfs(node, depth):
            if node:
                d[depth].append(node.val)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root, 0)
        return [d[depth] for depth in sorted(d)]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print sol.levelOrder(root)
