# Ref: https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1470959/JavaC%2B%2BPython-Match-from-the-Smallest-or-Biggest-100

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        c = collections.Counter(changed)
        if c[0] % 2 == 1:
            return []
        for n in sorted(c):  # need to sort the keys
            if c[n] > c[n * 2]:
                return []
            c[n * 2] -= c[n] if n > 0 else c[n] // 2  # keep half number of zeros to return
        return list(c.elements())
