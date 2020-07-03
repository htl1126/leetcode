# Ref: https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in nums:
            n = TreeNode(num)
            while stack and stack[-1].val < num:
                n.left = stack.pop()
            if stack:
                stack[-1].right = n
            stack.append(n)
        return stack[0]
        
if __name__ == "__main__":
    sol = Solution()
    print sol.constructMaximumBinaryTree()
