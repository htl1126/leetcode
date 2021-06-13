# Ref: https://leetcode.com/problems/missing-number-in-arithmetic-progression/discuss/408474/JavaC%2B%2BPython-Arithmetic-Sum-and-Binary-Search

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        d = (arr[-1] - arr[0]) // n
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] == arr[0] + m * d:
                l = m + 1
            else:
                r = m
        return arr[0] + l * d
