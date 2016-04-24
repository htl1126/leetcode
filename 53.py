# ref: https://leetcode.com/discuss/15805/accepted-o-n-solution-in-java


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxEndingHere = nums[0]
        maxSoFar = nums[0]
        for i in xrange(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar

if __name__ == '__main__':
    sol = Solution()
    print sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
