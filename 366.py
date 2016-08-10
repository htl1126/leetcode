import collections
# ref: https://discuss.leetcode.com/topic/49315/simple-python-solution-
#              using-dict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            lev = max(left, right)
            dic[lev].append(node.val)
            return lev
        dfs(root)
        return [dic[i] for i in xrange(1, len(dic) + 1)]

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print sol.findLeaves(root)
