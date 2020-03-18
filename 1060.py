# Ref: https://leetcode.com/problems/missing-element-in-sorted-array/discuss/305579/C%2B%2B-binary-search
# Ref: https://leetcode.com/problems/missing-element-in-sorted-array/discuss/307872/python-binary-search
# Algo: binary search

class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) / 2
            if nums[mid] >= nums[0] + mid + k:
                r = mid - 1
            else:
                l = mid
        return nums[0] + l + k


if __name__ == "__main__":
    sol = Solution()
    print sol.missingElement([4, 7, 9, 10], 3)
