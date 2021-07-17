# Ref: https://leetcode.com/problems/boundary-of-binary-tree/discuss/101308/python-dfs-solution
# Algo: DFS
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node is not root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary
        
if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    print sol.boundaryOfBinaryTree(root)
