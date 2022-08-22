# Ref: https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1211213/Python-Bitwise-OR-with-explanation-O(n)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_sum = 0
        for n in nums:
            or_sum |= n
        return or_sum * int(pow(2, len(nums) - 1))
