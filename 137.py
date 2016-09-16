# ref: https://discuss.leetcode.com/topic/34725/my-own-explanation-of-bit
#              -manipulation-method-might-be-easier-to-understand


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oneCtr, twoCtr = 0, 0
        for num in nums:
            oneCtr = (~twoCtr) & (oneCtr ^ num)
            twoCtr = (~oneCtr) & (twoCtr ^ num)
        return oneCtr

if __name__ == '__main__':
    sol = Solution()
    print sol.singleNumber([3, 3, 3, 1, 1, 1, 2])
