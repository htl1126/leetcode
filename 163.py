class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        nums = [lower - 1] * (lower < nums[0]) + nums + \
            [upper + 1] * (upper > nums[-1]) \
            if len(nums) > 0 else [lower - 1, upper + 1]
        for i in xrange(len(nums) - 1):
            if nums[i] + 2 == nums[i + 1]:
                ans.append(str(nums[i] + 1))
            elif nums[i] + 2 < nums[i + 1]:
                ans.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
