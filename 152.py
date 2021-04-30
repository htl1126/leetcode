# ref: https://leetcode.com/discuss/11923/sharing-my-solution-o-1-space-o-n-
#              running-time


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxherepre, minherepre, maxsofar = nums[0], nums[0], nums[0]
        maxhere, minhere = None, None
        for i in range(1, len(nums)):
            n = nums[i]
            maxhere = max(maxherepre * n, minherepre * n, n)
            minhere = min(maxherepre * n, minherepre * n, n)
            maxsofar = max(maxhere, maxsofar)
            maxherepre, minherepre = maxhere, minhere
        return maxsofar

if __name__ == '__main__':
    sol = Solution()
    print sol.maxProduct([2, 3, -2, 4])
