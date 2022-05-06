# Ref: https://leetcode.com/problems/count-binary-substrings/discuss/108625/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = ans = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                ans += min(cur, pre)
                pre = cur
                cur = 1
        return ans + min(cur, pre)
