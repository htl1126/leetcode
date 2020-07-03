# Ref: https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/99000/Python-BFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes
        
if __name__ == "__main__":
    sol = Solution()
    print sol.largestValues(root)
