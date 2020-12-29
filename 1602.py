# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root or root.val == u.val:
            return None
        level = [root]
        def add_node(level, node, u, pos):
            if node:
                level.append(node)
                if node.val == u.val:
                    pos[0] = len(level) - 1
        while level:
            new_level, pos = [], [-1]
            for node in level:
                add_node(new_level, node.left, u, pos)
                add_node(new_level, node.right, u, pos)
            if pos[0] >= 0:
                return None if pos[0] == len(new_level) - 1 else new_level[pos[0] + 1]
            level = new_level
        return None

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.findNearestRightNode(root, TreeNode(2)))
