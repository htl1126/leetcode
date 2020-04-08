# Ref: https://leetcode.com/problems/minimum-window-subsequence/discuss/109354/Python-O(m)-space-complexity-almost-O(n)-time-complexity
# Algo: dynamic programming

import collections

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = collections.defaultdict(list)
        for i, c in enumerate(T):
            dic[c].append(i)
        m = len(T)
        dp = [-1 for _ in xrange(m)]
        window_size, start = len(S) + 1, -1

        for index, c in enumerate(S):
            if c in dic:
                for i in dic[c][::-1]:
                    if i == 0:
                        dp[i] = index
                    else:
                        dp[i] = dp[i - 1]
                    if i == m - 1 and dp[i] >= 0 and index - dp[i] + 1 < window_size:
                        window_size = index - dp[i] + 1
                        start = dp[i]
        if dp[-1] < 0:
            return ""
        return S[start:start + window_size]

if __name__ == "__main__":
    sol = Solution()
    print sol.minWindow("abcdebdde", "bde")
