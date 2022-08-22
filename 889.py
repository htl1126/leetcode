# Ref: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre_index = post_index = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.pre_index])
        self.pre_index += 1
        if root.val != postorder[self.post_index]:
            root.left = self.constructFromPrePost(preorder, postorder)
        if root.val != postorder[self.post_index]:
            root.right = self.constructFromPrePost(preorder, postorder)
        self.post_index += 1
        return root
