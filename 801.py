# Ref: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119879/C%2B%2BJavaPython-DP-O(N)-Solution
# Algo: dynamic programming

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        swap, non_swap = [n for _ in xrange(n)], [n for _ in xrange(n)]
        swap[0], non_swap[0] = 1, 0
        for i in xrange(1, n):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                swap[i] = swap[i - 1] + 1
                non_swap[i] = non_swap[i - 1]
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                non_swap[i] = min(non_swap[i], swap[i - 1])
                swap[i] = min(swap[i], non_swap[i - 1] + 1)
        return min(swap[n - 1], non_swap[n - 1])

if __name__ == "__main__":
    sol = Solution()
    print sol.minSwap([1, 3, 5, 4], [1, 2, 3, 7])
