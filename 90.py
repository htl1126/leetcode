# ref: https://discuss.leetcode.com/topic/8541/simple-python-solution-without
#              -extra-space


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in xrange(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.subsetsWithDup([1, 2, 2])
