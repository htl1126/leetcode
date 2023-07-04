# Ref: https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/2832814/python-c-inorder-traversal-then-binary-search-explained/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(node, nums):
            if node:
                dfs(node.left, nums)
                nums.append(node.val)
                dfs(node.right, nums)

        nums = []
        dfs(root, nums)

        ans, n = [], len(nums)

        for q in queries:
            i = bisect_left(nums, q)
            if i < n and nums[i] == q:
                ans.append([q, q])
            else:
                if i == 0:
                    ans.append([-1, nums[0]])
                elif i == n:
                    ans.append([nums[-1], -1])
                else:
                    ans.append([nums[i - 1], nums[i]])

        return ans
