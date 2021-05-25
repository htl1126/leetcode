# Ref: https://leetcode.com/problems/rotate-array/discuss/54250/Easy-to-read-Java-solution

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            l, r = i, j
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        size = len(nums)
        k %= size
        if k == 0:
            return
        swap(0, size - 1)
        swap(0, k - 1)
        swap(k, size - 1)
