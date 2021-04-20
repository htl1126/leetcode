# Ref: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/502679/Python-3-One-Pass-O(N)-Time-O(N)-Space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        cur_n1, cur_n2 = root1, root2
        ans = []
        while cur_n1 or cur_n2 or stack1 or stack2:
            while cur_n1:
                stack1.append(cur_n1)
                cur_n1 = cur_n1.left
            while cur_n2:
                stack2.append(cur_n2)
                cur_n2 = cur_n2.left
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                cur_n1 = stack1.pop()
                ans.append(cur_n1.val)
                cur_n1 = cur_n1.right
            else:
                cur_n2 = stack2.pop()
                ans.append(cur_n2.val)
                cur_n2 = cur_n2.right
        return ans
