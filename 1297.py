# Ref: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/discuss/462213/Python-2-lines-Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
