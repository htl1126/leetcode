# Ref: https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100732/Short-compare-numsi-with-numsi1
# Algo: binary search

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == "__main__":
    sol = Solution()
    print sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
