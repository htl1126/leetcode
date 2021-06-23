# ref: https://discuss.leetcode.com/topic/39807/python-easy-o-n-solution


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:  # n > first and n <= second
                second = n
            else:              # n > first and n > second
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.increasingTriplet([1, 1, 1, 1])
