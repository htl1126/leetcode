# ref: https://leetcode.com/discuss/11923/sharing-my-solution-o-1-space-o-n-
#              running-time


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        maxherepre, minherepre, maxsofar = nums[0], nums[0], nums[0]
        maxhere, minhere = None, None
        for i in xrange(1, len(nums)):
            maxhere = max(max(maxherepre * nums[i], minherepre * nums[i]),
                          nums[i])
            minhere = min(min(maxherepre * nums[i], minherepre * nums[i]),
                          nums[i])
            maxsofar = max(maxhere, maxsofar)
            maxherepre = maxhere
            minherepre = minhere
        return maxsofar

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProduct([2, 3, -2, 4])
