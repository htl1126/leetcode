# ref: https://leetcode.com/problems/leaf-similar-trees/discuss/152329/C%2B%2BJavaPython-O(H)-Space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1, s2 = [root1], [root2]
        def dfs(stack):
            while True:
                node = stack[-1]
                stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                if not node.left and not node.right:
                    return node.val
        while s1 and s2:
            if dfs(s1) != dfs(s2):
                return False
        return not s1 and not s2
