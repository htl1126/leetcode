# Ref: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103052/Python-Sort-Solutions

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
