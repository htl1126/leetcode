# ref: https://discuss.leetcode.com/topic/16164/5-9-lines-python-48-ms/2


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root:
            level = [root]
            while level:
                ans.append(level[-1].val)
                level = [kid for node in level for kid in (node.left,
                                                           node.right) if kid]
        return ans

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print sol.rightSideView(root)
