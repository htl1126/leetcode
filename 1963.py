# Ref: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1390193/Python-Greedy-O(n)-explained

class Solution:
    def minSwaps(self, s: str) -> int:
        ans, bal = 0, 0
        for c in s:
            if c == '[':
                bal += 1
            else:
                bal -= 1
            ans = min(ans, bal)
        return (-ans + 1) // 2
