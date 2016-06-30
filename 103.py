# ref: https://leetcode.com/discuss/59912/python-simple-bfs


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, curr, stack, flag = [], [], [root], 1
        while stack:
            for _ in xrange(len(stack)):
                node = stack.pop(0)
                curr.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(curr[::flag])
            curr = []
            flag *= -1
        return ans

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print sol.zigzagLevelOrder(root)
