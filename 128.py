# ref: https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-
#              just-walk-each-streak


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best

if __name__ == '__main__':
    sol = Solution()
    print sol.longestConsecutive([100, 4, 200, 1, 3, 2])
