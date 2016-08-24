# ref: https://leetcode.com/discuss/46584/9-lines-ruby-11-lines-python-o-n
import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

if __name__ == '__main__':
    sol = Solution()
    print sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7])
