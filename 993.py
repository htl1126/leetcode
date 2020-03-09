# Ref: https://leetcode.com/problems/cousins-in-binary-tree/discuss/299889/Python-BFS-solution

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        node_map = collections.defaultdict(list)
        queue = [(root, 0, 0)]
        while queue:
            new_queue = []
            for node, level, parent in queue:
                node_map[node.val] = [level, parent]
                if node.left:
                    new_queue.append((node.left, level + 1, node.val))
                if node.right:
                    new_queue.append((node.right, level + 1, node.val))
            queue = new_queue
        if node_map[x][0] == node_map[y][0] and node_map[x][1] != node_map[y][1]:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print sol.isCousins(root, 5, 4)
