# Greedy solution
# For each (i, j), we just try to find next possible larger area.
# If height[i] < height[j], we won't get a larger area by j -= 1, so we do i += 1
# the similar case for height[i] > height[j]

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = -1
        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left += 1
            else:
                area = (right - left) * height[right]
                right -= 1
            if area > max_area:
                max_area = area
        return max_area
