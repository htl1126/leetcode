# Ref: https://leetcode.com/problems/finding-the-number-of-visible-mountains/

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        n = len(peaks)
        peaks.sort(key = lambda x: (x[0] - x[1], -(x[0] + x[1])))
        ans = 0
        max_right_end = float('-inf')
        
        for i, (x, y) in enumerate(peaks):
            if x + y > max_right_end:
                max_right_end = x + y
                if i < n - 1 and peaks[i] == peaks[i + 1]:
                    continue 
                ans += 1
        return ans
