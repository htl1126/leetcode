# ref: https://discuss.leetcode.com/topic/35494/solution-explanation


class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, added, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added

if __name__ == '__main__':
    sol = Solution()
    print sol.minPatches([1, 5, 10], 20)
