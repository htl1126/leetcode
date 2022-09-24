# Ref: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/discuss/927654/C%2B%2BJavaPython3-Simple-time-O(n)-space-O(1)-a-small-array-is-all-you-need

class Solution:
    def minDeletions(self, s: str) -> int:
        prev, keep = float('inf'), 0
        for freq in sorted(collections.Counter(s).values(), reverse=True):
            freq = min(prev - 1, freq)
            if freq == 0:
                break
            keep += freq
            prev = freq
        return len(s) - keep
