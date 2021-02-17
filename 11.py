# Greedy solution
# For each (i, j), we just try to find next possible larger area.
# If height[i] < height[j], we won't get a larger area by j -= 1, so we do i += 1
# the similar case for height[i] > height[j]

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        l, r = 0, len(height) - 1
        while l < r:
            maxA = max(maxA, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA
