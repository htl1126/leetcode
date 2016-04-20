# ref: https://leetcode.com/discuss/53530/python-different-solutions-
#              comments-bubble-selection-quick


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    def partition(self, nums, l, r):  # do partitioning in-place
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[low], nums[l] = nums[l], nums[low]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

if __name__ == '__main__':
    sol = Solution()
    print sol.findKthLargest([1, 2, 7, 3, 6, 5])
