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

# faster solution, source: https://leetcode.com/discuss/70274/56-ms-python-solution

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        summ = sum(nums[-3:])
        if target >= summ: return summ
        closest = sum(nums[:3])
        if target <= closest: return closest

        diff = abs(closest - target)

        for i in range(len(nums) - 2):
            # Look for the second number:
            # From index i + 1, find the smallest number nums[left] such that
            # nums[left] >= target - nums[i] - nums[-1]
            left = bisect.bisect_left(nums, target - nums[i] - nums[-1], lo=i + 1)
            # We can try nums[left - 1] if left > i + 1
            if left > i + 1:
                left -= 1
            for j in range(left, len(nums) - 1):
                num2find = target - nums[i] - nums[j]
                # Look for the third number:
                # From index j + 1, find the smallest number nums[ind] such that
                # nums[ind] >= target - nums[i] - nums[j]
                ind = bisect.bisect_left(nums, num2find, lo=j + 1)
                # We try both nums[ind - 1] and nums[ind]
                values = [ind - 1, ind]
                for val in values:
                    if val > j and val < len(nums):
                        summ = nums[i] + nums[j] + nums[val]
                        if summ == target:
                            return target
                        if abs(summ - target) < diff:
                            closest = summ
                            diff = abs(summ - target)
                # current j is the largest index for the second number
                if nums[i] + nums[j] + nums[j + 1] > target:
                    break
        return closest

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSumClosest([-1, 2, 1, -4], 1)
