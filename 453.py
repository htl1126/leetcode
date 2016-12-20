# ref: https://discuss.leetcode.com/topic/66562/simple-one-liners

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)

if __name__ == '__main__':
    sol = Solution()
    print sol.minMoves([1, 2, 3])
