# Ref: https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/discuss/2112243/JavaC%2B%2BPython-Sort-%2B-Greedy

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        v_min = v_max = nums[0]
        for n in nums:
            v_min = min(v_min, n)
            v_max = max(v_max, n)
            if v_max - v_min > k:
                ans += 1
                v_min = v_max = n
        # the initial value for ans is 1
        # so in the whole loop ans doesn't get update, the answer is correct
        # and even though ans > 1, the last partition will get counted
        return ans
