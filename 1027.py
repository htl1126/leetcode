# Ref: https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC%2B%2BPython-DP
# Algo: dynamic programming

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i):
                dp[i, A[i] - A[j]] = dp.setdefault((j, A[i] - A[j]), 1) + 1
        return max(dp.values())

if __name__ == "__main__":
    sol = Solution()
    print sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8])
