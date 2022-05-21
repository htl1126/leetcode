# Ref: https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/113536/Python-Easy-Understood-Solution

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans, cur_max = 0, -1
        for i, v in enumerate(arr):
            cur_max = max(cur_max, v)
            if cur_max == i:
                ans += 1
        return ans
