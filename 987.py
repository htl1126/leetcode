# Ref: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231256/python-queue-%2B-hash-map

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            cur_level = collections.defaultdict(list)
            new = []
            for node, i in queue:
                cur_level[i].append(node.val)
                if node.left:
                    new.append((node.left, i - 1))
                if node.right:
                    new.append((node.right, i + 1))
            for i in cur_level:
                res[i] += sorted(cur_level[i])
            queue = new
        return [res[i] for i in sorted(res)]

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.verticalTraversal(root)
