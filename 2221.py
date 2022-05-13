# Ref: https://leetcode.com/problems/find-triangular-sum-of-an-array/discuss/1907380/O(n)-time-O(1)-space-Python-189-ms-C%2B%2B-12-ms-Java-4-ms

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        coef, n, ans = 1, len(nums) - 1, nums[0] % 10
        for i in range(1, len(nums)):
            coef = coef * (n - i + 1) // i
            ans += (coef * nums[i]) % 10
        return ans % 10
