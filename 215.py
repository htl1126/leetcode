# ref: https://leetcode.com/discuss/53530/python-different-solutions-
#              comments-bubble-selection-quick

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = self.partition(nums, 0, len(nums) - 1)
        if pos == k - 1:
            return nums[pos]
        elif pos < k - 1:
            return self.findKthLargest(nums[pos + 1:], k - pos - 1)
        else:
            return self.findKthLargest(nums[:pos], k)
        
    def partition(self, nums, lo, hi):
        pivot = random.randint(lo, hi)
        nums[pivot], nums[hi] = nums[hi], nums[pivot]
        low, l = lo, lo
        # place larger numbers behind the pivot and small numbers after the pivot
        while l < hi:
            if nums[l] > nums[hi]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[hi] = nums[hi], nums[low]
        return low

if __name__ == '__main__':
    sol = Solution()
    print sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
