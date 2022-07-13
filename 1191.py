# Ref: https://leetcode.com/problems/k-concatenation-maximum-sum/discuss/382808/Python3-6-liner-Kadane

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def find_max_subarray_sum(nums):
            cur = ans = 0
            for n in nums:
                cur = max(n, n + cur)
                ans = max(ans, cur)
            return ans
        if k > 1:
            return ((k - 2) * max(sum(arr), 0) + find_max_subarray_sum(arr * 2)) % (10 ** 9 + 7)
        else:
            return find_max_subarray_sum(arr) % (10 ** 9 + 7)
