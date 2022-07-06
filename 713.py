# Ref: https://leetcode.com/problems/subarray-product-less-than-k/discuss/868623/Python-2-pointers-O(n)-solution-explained

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, i, j, cur = 0, 0, 0, 1
        while j < len(nums):
            cur *= nums[j]
            while i <= j and cur >= k:
                cur //= nums[i]
                i += 1
            ans += j - i + 1
            j += 1
        return ans
