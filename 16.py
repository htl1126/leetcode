# ref:


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        for i in xrange(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum([nums[i], nums[l], nums[r]])
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    break
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSumClosest([-1, 2, 1, -4], 1)
