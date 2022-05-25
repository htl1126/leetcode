# Ref: https://leetcode.com/problems/delete-operation-for-two-strings/discuss/1195726/C%2B%2BPythonJava-Short-and-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
