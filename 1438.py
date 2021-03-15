# Ref: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)

import collections
import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for n in nums:
            while maxd and n > maxd[-1]:
                maxd.pop()
            while mind and n < mind[-1]:
                mind.pop()
            maxd.append(n)
            mind.append(n)
            # We only remove one element in one iteration. If we remove more than one element,
            # 'i' won't keep the optimal solution anymore. Therefore, len(nums) - i would be the
            # answer.
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]:
                    maxd.popleft()
                if mind[0] == nums[i]:
                    mind.popleft()
                i += 1
        return len(nums) - i

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxh, minh = [], []
        res = i = 0
        for j, n in enumerate(nums):
            heapq.heappush(maxh, [-n, j])
            heapq.heappush(minh, [n, j])
            while -maxh[0][0] - minh[0][0] > limit:
                i = min(maxh[0][1], minh[0][1]) + 1
                while maxh[0][1] < i:
                    heapq.heappop(maxh)
                while minh[0][1] < i:
                    heapq.heappop(minh)
            res = max(res, j - i + 1)
        return res
