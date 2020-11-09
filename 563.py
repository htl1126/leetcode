# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]
        def getSubTreeSum(node):
            if node:
                left_sum = getSubTreeSum(node.left)
                right_sum = getSubTreeSum(node.right)
                ans[0] += abs(left_sum - right_sum)
                return node.val + left_sum + right_sum
            else:
                return 0
        getSubTreeSum(root)
        return ans[0]

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    print sol.findTilt(root)
