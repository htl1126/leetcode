# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count_uni_subtree(node):
            if not node:
                return True, 0
            left_flag, left_count = count_uni_subtree(node.left)
            right_flag, right_count = count_uni_subtree(node.right)
            print node.val, left_count, right_count
            if left_flag and right_flag:
                vals = [n.val for n in (node.left, node.right) if n]
                if all(val == node.val for val in vals):
                    return True, left_count + right_count + 1
                return False, left_count + right_count
            else:
                return False, left_count + right_count
        _, ans = count_uni_subtree(root)
        return ans

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print sol.countUnivalSubtrees(root)
