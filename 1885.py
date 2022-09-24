# Ref: https://leetcode.com/problems/count-pairs-in-two-arrays/discuss/1249691/Python-binary-search-with-explanation

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums = [x - y for x, y in zip(nums1, nums2)]
        nums.sort()
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            # find the smallest nums[idx] such that
            # nums[idx] >= -x + 1, so nums[idx] + x >= 1 > 0
            idx = bisect.bisect_left(nums, -x + 1)
            ans += n - max(i + 1, idx)  # use i + 1 to avoid duplicates
        return ans
