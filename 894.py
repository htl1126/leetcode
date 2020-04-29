# Ref: https://leetcode.com/problems/all-possible-full-binary-trees/discuss/163429/Simple-Python-recursive-solution.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, N, memos = {1: [TreeNode(0)]}):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N in memos:
            return memos[N]
        ans = []
        for i in xrange(1, N - 1, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - 1 - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
        memos[N] = ans
        return ans

if __name__ == "__main__":
    sol = Solution()

