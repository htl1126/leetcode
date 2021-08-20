# ref: https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/C%2B%2BJavaPython-Better-than-Binary-Search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l
