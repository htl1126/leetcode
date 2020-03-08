# Ref: https://leetcode.com/problems/sort-an-array/discuss/277127/7-line-quicksort-to-write-in-interviews-(Python)

import random

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        pivot = random.choice(nums)
        lt = [v for v in nums if v < pivot]
        eq = [v for v in nums if v == pivot]
        gt = [v for v in nums if v > pivot]
        return self.sortArray(lt) + eq + self.sortArray(gt)
        
if __name__ == "__main__":
    sol = Solution()
    print sol.sortArray([5, 2, 3, 1])
