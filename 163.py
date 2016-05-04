# ref: https://leetcode.com/discuss/29207/ten-line-python-solution


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        nums.append(upper + 1)
        pre = lower - 1
        for i in nums:
            if i == pre + 2:
                result.append(str(i - 1))
            elif i > pre + 2:
                result.append('{0}->{1}'.format(pre + 1, i - 1))
            pre = i
        return result

if __name__ == '__main__':
    sol = Solution()
    print sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
