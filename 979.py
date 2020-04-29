# Ref: https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221930/JavaC%2B%2BPython-Recursive-Solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root, pre=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre:
            pre.val += root.val - 1
        return res + abs(root.val - 1)
        
if __name__ == "__main__":
    sol = Solution()
    print sol.distributeCoins()
