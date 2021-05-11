# ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48908/Clean-python-solution


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

if __name__ == '__main__':
    sol = Solution()
    print sol.findMin([1, 2, 3, 4, 5])
