# Ref: https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/discuss/101520/DFS-C%2B%2B-Python-solutions

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, parent):
            if not node:
                return 0, 0
            # left_inc/right_inc: length of longest increasing sequence starting from 'node'
            left_inc, left_dec = dfs(node.left, node)
            right_inc, right_dec = dfs(node.right, node)
            l[0] = max(l[0], left_inc + right_dec + 1, left_dec + right_inc + 1)
            if node.val == parent.val + 1:
                return max(left_inc, right_inc) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(left_dec, right_dec) + 1
            return 0, 0
        l = [0]  # if we use l (not a list) it won't be accessed by dfs()
        dfs(root, root)
        return l[0]
        
if __name__ == "__main__":
    sol = Solution()
    print sol.longestConsecutive(root)
