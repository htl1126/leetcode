# Ref: https://leetcode.com/problems/find-duplicate-subtrees/discuss/106020/Python-easy-understand-solution

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def dfs(node):
            if not node:
                return "null"
            struct = "{0},{1},{2}".format(str(node.val), dfs(node.left), dfs(node.right))
            nodes[struct].append(node)
            return struct
        nodes = collections.defaultdict(list)
        dfs(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]

if __name__ == "__main__":
    sol = Solution()
    print sol.findDuplicateSubtrees(root)
