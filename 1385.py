# Ref: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/discuss/546484/Python-1-Line

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)
