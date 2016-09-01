# ref: https://discuss.leetcode.com/topic/19931/6-line-java-solution-in-o-n


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = 0
        for i in xrange(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.canJump([2, 3, 1, 1, 4])
