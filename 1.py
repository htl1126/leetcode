import sys

# Extended prob: what if there are multiple targets?

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup_dict = {}
        for i in xrange(len(nums)):
            if nums[i] in lookup_dict:
                return [lookup_dict[nums[i]], i + 1]
            else:
                lookup_dict[target - nums[i]] = i + 1

if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum([2, 7, 11, 15], 9)
