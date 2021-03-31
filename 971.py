# Ref: https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/discuss/214216/JavaC%2B%2BPython-DFS-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack, res = [root], []
        i = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val != voyage[i]:
                return [-1]
            i += 1
            if node.right and node.right.val == voyage[i]:
                if node.left:
                    res.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
        return res
