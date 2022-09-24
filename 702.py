# Ref: https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/discuss/303196/Python-Solution-using-Binary-Search-beats-99.53

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, 1

        while reader.get(r) < target:
            l = r
            r <<= 1

        while l <= r:
            m = (l + r) >> 1
            if reader.get(m) == target:
                return m
            elif reader.get(m) > target:
                r = m - 1
            else:
                l = m + 1
        return -1
