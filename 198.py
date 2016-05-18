# ref: https://leetcode.com/discuss/42398/python-solution-3-lines


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        table = [0 for _ in xrange(len(nums))]
        table[0] = nums[0]
        for i in xrange(1, len(nums)):
            if i < 2:
                table[i] = max(table[0], nums[1])
            else:
                table[i] = max(table[i - 1], nums[i] + table[i - 2])
        return table[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.rob([1, 2])
