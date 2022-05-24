# Ref: https://leetcode.com/problems/minimum-number-of-keypresses/discuss/2027810/Python-3-or-Greedy-or-Explanation

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = collections.Counter(s)
        ans = count = 0
        for i, freq in enumerate(sorted(c.values(), reverse=True)):
            if i % 9 == 0:
                count += 1
            ans += count * freq
        return ans
