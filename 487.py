# Ref: https://leetcode.com/problems/max-consecutive-ones-ii/discuss/96946/Concise-Python-solution-good-for-follow-up-time-O(n)-space-O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre, cur, ans = -1, 0, 0
        for n in nums:
            if n == 0:
                pre, cur = cur, 0
            else:
                cur += 1
            ans = max(ans, pre + 1 + cur)
        return ans
