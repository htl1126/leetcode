# ref: https://leetcode.com/discuss/16171/sharing-my-simple-c-code-o-n
#              -time-o-1-space


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxleft, maxright = 0, 0
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    ans += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    ans += maxright - height[right]
                right -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
