class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max, global_max = 0, 0
        for num in nums:
            if num == 0:
                cur_max = 0
            else:
                cur_max += 1
                global_max = max(cur_max, global_max)
        return global_max

if __name__ == '__main__':
    sol = Solution()
    print sol.findMaxConsecutiveOnes([0])
