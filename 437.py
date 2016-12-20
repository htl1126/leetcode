# ref: https://discuss.leetcode.com/topic/64396/easy-recursive
#              -python-7-lines-solution

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
        :rtype: int
        """
        return self.find(root, sum, [sum])

    def find(self, node, target, sums):
        if not node:
            return 0
        hit = 0
        hit += sum(s - node.val == 0 for s in sums)
        sums = [s - node.val for s in sums] + [target]
        return (hit + self.find(node.left, target, sums) +
                 self.find(node.right, target, sums))

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    print sol.pathSum(root, 8)
