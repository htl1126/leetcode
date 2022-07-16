# Ref: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/discuss/2138951/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = cur = i = 0
        for j in range(len(nums)):
            cur += nums[j]
            while cur * (j - i + 1) >= k:
                cur -= nums[i]
                i += 1
            ans += j - i + 1
        return ans
