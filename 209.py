# ref: https://discuss.leetcode.com/topic/14288/python-o-n-and-o-n
#              -log-n-solution


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result, total, l, r = len(nums) + 1, 0, 0, 0
        for idx, num in enumerate(nums):
            total += num
            r = idx
            while total >= s:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1
        return result if result <= len(nums) else 0

if __name__ == '__main__':
    sol = Solution()
    print sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
