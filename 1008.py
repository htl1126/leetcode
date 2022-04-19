# Ref: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/discuss/252232/JavaC%2B%2BPython-O(N)-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build_tree(nodes, bound):
            # not nodes: nodes are all taken
            # nodes[-1] > bound: nodes are not the children of the current node
            if not nodes or nodes[-1] > bound:
                return None
            node = TreeNode(nodes.pop())
            node.left = build_tree(nodes, node.val)
            # at this point, nodes with value less than node.val will be taken
            node.right = build_tree(nodes, bound)
            return node
        return build_tree(preorder[::-1], float('inf'))
