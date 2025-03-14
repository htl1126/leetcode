class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        cur = 0

        i = 0
        while i < len(nums) - 1:
            if nums[i] != 0:
                if nums[i] == nums[i + 1]:
                    ans[cur] = nums[i] * 2
                    i += 1
                else:
                    ans[cur] = nums[i]
                cur += 1
            i += 1

        if i < len(nums) and nums[i] != 0:
            ans[cur] = nums[i]

        return ans

