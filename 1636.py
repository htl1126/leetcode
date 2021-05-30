# Ref: https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/917795/C%2B%2BPython-Sort

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))
