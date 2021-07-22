# ref: https://discuss.leetcode.com/topic/31121/python-solution
import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, d = [(0, root)], collections.defaultdict(list)
        while queue:
            new = []
            for i, node in queue:
                d[i].append(node.val)
                if node.left:
                    new.append((i - 1, node.left))
                if node.right:
                    new.append((i + 1, node.right))
            queue = new
        return [d[i] for i in sorted(d)]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.verticalOrder(root)
