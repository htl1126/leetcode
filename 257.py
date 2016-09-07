# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths = []

        def find_path(node, cur_path):
            if not node.left and not node.right:
                paths.append('->'.join(cur_path + [str(node.val)]))
            else:
                if node.left:
                    find_path(node.left, cur_path + [str(node.val)])
                if node.right:
                    find_path(node.right, cur_path + [str(node.val)])
        if root:
            find_path(root, [])
        return paths

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print sol.binaryTreePaths(root)
