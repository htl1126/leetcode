# ref: https://discuss.leetcode.com/topic/67539/0-1-knapsack-detailed-explanation


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 == 1:
            return False
        nums.sort()
        dp = [1] + [0] * sum(nums)
        pre_dp = [1] + [0] * sum(nums)
        curr_sum = 0
        for num in nums:
            curr_sum += num
            for i in xrange(1, curr_sum + 1):
                if i >= num:
                    dp[i] |= pre_dp[i - num]
            pre_dp = dp[:]
        return dp[curr_sum /  2] == 1

if __name__ == '__main__':
    sol = Solution()
    print sol.canPartition([2, 2, 3, 5])
