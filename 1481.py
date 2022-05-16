# Ref: https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/discuss/686343/Python-oror-3-Line-oror-Shortest-Simplest

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        # use key (count[x], x) to make the same numbers sorted together
        # Ex:
        # (count[x]) has 24, 157, 373, 24, 82, 157, 82, 373
        # (count[x], x) has 24, 24, 82, 82, 157, 157, 373, 373
        s = sorted(arr, key=lambda x: (count[x], x))
        return len(set(s[k:]))
