# Ref: https://leetcode.com/problems/squares-of-a-sorted-array/discuss/283978/Python-Two-Pointers

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = [None for _ in xrange(len(A))]
        left, right = 0, len(A) - 1
        for i in xrange(len(A) - 1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                ans[i] = A[left] ** 2
                left += 1
            else:
                ans[i] = A[right] ** 2
                right -= 1
        return ans

if __name__ == "":
    sol = Solution()
    print sol.sortedSquares([-4,-1,0,3,10])
