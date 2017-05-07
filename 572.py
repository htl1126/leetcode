# ref: https://discuss.leetcode.com/topic/88533/short-python-by-converting-into
#              -strings

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(a):
            return '^' + str(a.val) + '#' + convert(a.left) + \
                    convert(a.right) if a else '$'
        return convert(t) in convert(s)

if __name__ == '__main__':
    sol = Solution()
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    print sol.isSubtree(s, t)
