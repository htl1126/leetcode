class Solution:
    def check(self, nums: List[int]) -> bool:
        idx = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if idx == -1:
                    idx = i
                else:
                    return False
        if idx >= 0:
            return nums[-1] <= nums[0]
        return True
