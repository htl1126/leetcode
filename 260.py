# ref: https://discuss.leetcode.com/topic/21605/accepted-c-java-o-n-time-o-1
#              -space-easy-solution-with-detail-explanations


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        # set the right most different bit of the two single numbers to 1
        diff &= -diff
        res = [0, 0]
        for num in nums:
            if num & diff:
                res[0] ^= num
            else:
                res[1] ^= num
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.singleNumber([1, 2, 1, 3, 2, 5])
