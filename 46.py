# ref: https://leetcode.com/discuss/18212/my-elegant-recursive
#              -c-solution-with-inline-explanation
# ref: https://discuss.leetcode.com/topic/17277/one-liners-in-python


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return nums and [p[:i] + [nums[0]] + p[i:]
                         for p in self.permute(nums[1:])
                         for i in xrange(len(nums))] or [[]]

if __name__ == '__main__':
    sol = Solution()
    print sol.permute([1, 2])
