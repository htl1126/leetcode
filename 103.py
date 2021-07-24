# ref: https://leetcode.com/discuss/59912/python-simple-bfs


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level, direction = [], [root], 1
        while level:
            res.append([n.val for n in level][::direction])
            direction *= -1
            level = [kid for node in level for kid in (node.left, node.right)
                     if kid]
        return res

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.zigzagLevelOrder(root)
