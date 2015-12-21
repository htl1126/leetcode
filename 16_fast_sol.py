class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # Check cases where target exceeds lowest and highest possible sums
        summ = sum(nums[-3:])
        if target >= summ: return summ
        closest = sum(nums[:3]) #initialize closest
        if target <= closest: return closest

        # Keep track of closest difference
        diff = abs(closest - target)

        # Iterate with restriction that first number index < second number index < third number index
        # Iterate leftmost number
        for i in xrange(len(nums) - 2):

            # Index of smallest possibility for second number: target - first num - greatest possible num
            left = bisect.bisect_left(nums, target - nums[i] - nums[-1], lo = i + 1) #binary search
            if left > i + 1: left -= 1 #Start checking the number just below

            # Iterate second number
            for j in xrange(left, len(nums) - 1):
                # Find the values closest to the number that would hit target
                num2find = target - nums[i] - nums[j]
                ind = bisect.bisect_left(nums, num2find, j + 1) #binary search

                # Check value just below and num
                values = [ind - 1, ind]
                for val in values:
                    if val > j and val < len(nums):
                        summ = nums[i] + nums[j] + nums[val]
                        if summ == target:
                            return target
                        if abs(summ - target) < diff:
                            closest = summ
                            diff = abs(summ - target)
                # Don't bother iterating through second number anymore after target is exceeded
                if nums[i] + nums[j] + nums[j + 1] > target: break
        return closest
