# ref: https://discuss.leetcode.com/topic/26019/5-lines-o-n-python-with
#              -explanation


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, last, next, n = 0, 0, 0, len(nums)
        while next < n - 1:
            ans += 1
            last, next = next, max(i + nums[i] for i in xrange(last, next + 1))
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.jump([2, 3, 1, 1, 4])
