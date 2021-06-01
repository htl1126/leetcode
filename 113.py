# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        def find_path(node, path, current_sum, target):
            if current_sum == target and not node.left and not node.right:
                result.append(path)
            if node.left:
                find_path(node.left, path + [node.left.val], current_sum + node.left.val, target)
            if node.right:
                find_path(node.right, path + [node.right.val], current_sum + node.right.val, target)
        if root:
            find_path(root, [root.val], root.val, targetSum)
        return result

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print sol.pathSum(root, 1)
