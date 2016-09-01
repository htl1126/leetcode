# ref: https://discuss.leetcode.com/topic/14375/simple-ac-solution-in-java-in-o
#              -n-with-explanation


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def solve_sub(lo, hi):
            tbl = [nums[lo]] + [0] * (hi - lo)
            for i in xrange(hi - lo + 1):
                if i < 2:
                    tbl[i] = max(nums[lo + i], tbl[0])
                else:
                    tbl[i] = max(nums[lo + i] + tbl[i - 2], tbl[i - 1])
            print tbl
            return tbl[-1]
        return max(solve_sub(0, len(nums) - 2), solve_sub(1, len(nums) - 1))

if __name__ == '__main__':
    sol = Solution()
    print sol.rob([2, 1, 1, 2])
