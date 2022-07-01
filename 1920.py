# Ref: https://leetcode.com/problems/build-array-from-permutation/discuss/1315926/Python-O(n)-Time-O(1)-Space-w-Full-Explanation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i in range(q):
            r = nums[i]  # nums[i], nums[i + 1], ... have not been updated yet
            b = nums[nums[i]] % q
            nums[i] = b * q + r
        for i in range(q):
            nums[i] //= q
        return nums
