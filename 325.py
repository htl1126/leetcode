# ref: https://leetcode.com/discuss/78044/clean-python-solution-one-pass
# DP solution


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acc, ans = 0, 0
        mp = {0: -1}
        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in mp:
                mp[acc] = i
            if acc - k in mp:
                ans = max(ans, i - mp[acc - k])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.maxSubArrayLen([1, -1, 5, -2, 3], 3)
