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
        if not root:
            return paths

        def get_path(node, path):
            if not node.left and not node.right:
                paths.append('->'.join(str(item) for item in path + [node.val]))
            else:
                if node.left:
                    get_path(node.left, path + [node.val])
                if node.right:
                    get_path(node.right, path + [node.val])
        get_path(root, [])
        return paths

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print sol.binaryTreePaths(root)
