# Ref: https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996390/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation

class Solution:
    def appealSum(self, s: str) -> int:
        last = collections.defaultdict(lambda: -1)
        n, ans = len(s), 0
        for i, c in enumerate(s):
            ans += (i - last[c]) * (n - i)
            last[c] = i
        return ans
