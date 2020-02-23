# Ref: https://leetcode.com/problems/two-sum-bsts/discuss/397608/Python3-4-liner

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        def dfs(node):
            return dfs(node.left) | dfs(node.right) | {node.val} if node else set()
        set1 = dfs(root1)
        return any(target - a in set1 for a in dfs(root2))

if __name__ == "":
    sol = Solution()
    print sol.twoSumBSTs()
