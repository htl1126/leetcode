# Ref: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/discuss/1676865/Python3-Java-C%2B%2B-Easy-Sliding-Window-O(n)

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = nums.count(1)
        nums = nums + nums
        cur_max, total_max = 0, 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones] == 1:
                cur_max -= 1
            if nums[i] == 1:
                cur_max += 1
            total_max = max(cur_max, total_max)
        return ones - total_max
