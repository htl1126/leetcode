#Ref: https://leetcode.com/problems/longest-mountain-in-array/discuss/135593/C%2B%2BJavaPython-1-pass-and-O(1)-space

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = up = down = 0
        for i in xrange(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]:
                up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down:
                res = max(res, up + down + 1)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.longestMountain([2, 1, 4, 7, 3, 2, 5])
