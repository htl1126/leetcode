# ref: https://leetcode.com/discuss/18212/my-elegant-recursive
#              -c-solution-with-inline-explanation


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, res)
        return res

    def dfs(self, nums, begin, res):
        if begin == len(nums):
            if nums not in res:
                res.append(nums[:])
        else:
            for i in xrange(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                self.dfs(nums, begin + 1, res)
                nums[i], nums[begin] = nums[begin], nums[i]

if __name__ == '__main__':
    sol = Solution()
    print sol.permute([1, 1, 2])
