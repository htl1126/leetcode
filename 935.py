# Ref: https://leetcode.com/problems/knight-dialer/discuss/189287/O(n)-time-O(1)-space-DP-solution-%2B-Google-interview-question-writeup

class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        memo = {}
        def helper(i, n):
            if n == 1:
                return 1
            if (i, n) not in memo:
                memo[i, n] = 0
                for neighbor in neighbors[i]:
                    memo[i, n] += helper(neighbor, n - 1)
                memo[i, n] %= 10 ** 9 + 7
            return memo[i, n]
        ans = sum(helper(i, n) for i in range(10)) % (10 ** 9 + 7)
        return ans
