# Ref: https://leetcode.com/problems/print-binary-tree/discuss/106240/Python-recursive-solution-easy-to-understand

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        output = None
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))
        def update_output(node, row, left, right):
            if node:
                mid = (left + right) / 2
                output[row][mid] = str(node.val)
                update_output(node.left, row + 1, left, mid - 1)
                update_output(node.right, row + 1, mid + 1, right)
        r = get_height(root)
        output = [["" for _ in xrange(2 ** r - 1)] for _ in xrange(r)]
        update_output(root, 0, 0, 2 ** r - 1)
        return output

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print sol.printTree(root)
