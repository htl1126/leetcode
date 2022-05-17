# Ref: https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = ans = count = 0
        for j in range(len(nums)):
            # when nums[j] is odd, we reset 'count' for sequences ending at nums[j]
            # otherwise, we keep 'count' for sequences ending at nums[j] which is even
            if nums[j] & 1 == 1:
                k -= 1
                count = 0  # reset for counting sequence ending at nums[j]
            while k == 0:  # when we have k odd numbers in the sequence
                k += nums[i] & 1
                i += 1
                count += 1
            ans += count
        return ans
