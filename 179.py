class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(a, b):
            return [1, -1][a + b > b + a]
        nums = sorted([str(num) for num in nums], compare)
        return ''.join(nums).lstrip('0') or '0'
