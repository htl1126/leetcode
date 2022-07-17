# Ref: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/128952/JavaC%2B%2BPython-One-pass-O(N)

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        ans = 0
        for i, c in enumerate(s):
            k, j = index[c]
            ans += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            ans += (len(s) - j) * (j - k)
        return ans % (10 ** 9 + 7)
