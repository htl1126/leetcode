# ref: https://leetcode.com/discuss/4220/a-very-nice-solution-from-ants
#              -aasma-%40stackoverflow


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in xrange(length):
            pick = nums[i]
            while 0 < pick <= length and nums[pick - 1] != pick:
                tmp = nums[pick - 1]
                nums[pick - 1] = pick
                pick = tmp
        for i in xrange(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

if __name__ == '__main__':
    sol = Solution()
    print sol.firstMissingPositive([-3, 9, 16, 4, 5, 16, -4, 9, 26, 2])
