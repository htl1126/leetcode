# Ref: https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        i = s.find("(")
        if i < 0:
            return TreeNode(val=int(s)) if s else None
        balance = 0
        for j, c in enumerate(s):
            if c == "(":
                balance += 1
            if c == ")":
                balance -= 1
            if j > i and balance == 0:
                break
        root = TreeNode(val=int(s[:i]))
        root.left = self.str2tree(s[i + 1:j])
        root.right = self.str2tree(s[j + 2:-1])
        return root
