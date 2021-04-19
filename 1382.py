# Ref: https://leetcode.com/problems/balance-a-binary-search-tree/discuss/540038/python-3-easy-to-understand

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                inorder.append(node)
                dfs(node.right)
                
        def gen_bst(node_list):
            if node_list == []:
                return None
            root_i = len(node_list) // 2
            root = node_list[root_i]
            root.left = gen_bst(node_list[:root_i])
            root.right = gen_bst(node_list[root_i + 1:])
            return root
        
        dfs(root)
        return gen_bst(inorder)
