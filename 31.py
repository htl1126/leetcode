class Solution(object):
    def nextPermutation(self, nums):
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return

        k = i - 1
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]

        l, r = i, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 5, 4, 3]
    sol.nextPermutation(nums)
    print(nums)
