# Ref: https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python

class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        end = float("-inf")
        erased = 0
        for i in sorted(intervals, key=lambda x: x[1]):
            if i[0] >= end:
                end = i[1]
            else:
                erased += 1
        return erased

if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
