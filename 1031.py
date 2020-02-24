# Ref: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/278251/JavaC%2B%2BPython-O(N)Time-O(1)-Space
# Algo: dynamic programming

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        for i in xrange(1, len(A)):
            A[i] += A[i - 1]
        ans, maxL, maxM = A[L + M - 1], A[L - 1], A[M - 1]
        for i in xrange(L + M, len(A)):
            maxL = max(maxL, A[i - M] - A[i - M - L])
            maxM = max(maxM, A[i - L] - A[i - L - M])
            ans = max(ans, maxL + A[i] - A[i - M], maxM + A[i] - A[i - L])
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)
