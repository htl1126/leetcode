# Ref: https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/C%2B%2BJavaPython-Sliding-Window-O(1)-Space

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(s):
            if s < 0:
                return 0
            ans = i = 0
            for j in range(len(nums)):
                s -= nums[j]
                while s < 0:
                    s += nums[i]
                    i += 1
                ans += j - i + 1
            return ans
        return at_most(goal) - at_most(goal - 1)
