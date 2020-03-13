# Ref: https://leetcode.com/problems/sliding-window-median/discuss/96355/Easy-Python-O(nk)

import bisect

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k / 2] + window[~(k / 2)]) / 2.0)
            window.remove(a)
            bisect.insort(window, b)
        return medians

if __name__ == "__main__":
    sol = Solution()
    print sol.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
