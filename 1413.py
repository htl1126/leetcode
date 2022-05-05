class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans, cur = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur += nums[i]
            ans = min(cur, ans)
        return -ans + 1 if ans < 0 else 1
