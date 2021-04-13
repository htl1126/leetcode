import collections

class Solution:
    def numSplits(self, s: str) -> int:
        d1, d2 = collections.Counter(), collections.Counter(s)
        ans = 0
        for i in range(len(s) - 1):
            d1[s[i]] += 1
            d2[s[i]] -= 1
            if not d2[s[i]]:
                del d2[s[i]]
            if len(d1) == len(d2):
                ans += 1
        return ans
