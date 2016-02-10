# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        def find_path(node, path, current_sum, sum, result):
            if current_sum == sum and not node.left and not node.right:
                result.append(path)
            if node.left:
                find_path(node.left, path + [node.left.val], current_sum + node.left.val, sum, result)
            if node.right:
                find_path(node.right, path + [node.right.val], current_sum + node.right.val, sum, result)
        if root:
            find_path(root, [root.val], root.val, sum, result)
        return result

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print sol.pathSum(root, 1)
