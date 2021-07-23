# Ref: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/278271/JavaC%2B%2BPython-Sliding-Window-O(N)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = maxfreq = 0  # res is the current longest result sequence size up to index i
        count = collections.defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            maxfreq = max(maxfreq, count[s[i]])
            if res - maxfreq < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res
