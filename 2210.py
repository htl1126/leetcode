class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        pre, cur = 0, 1
        ans = 0
        for i in range(2, len(nums)):
            if nums[cur] != nums[i]:
                if nums[pre] > nums[cur] < nums[i] or nums[pre] < nums[cur] > nums[i]:
                    ans += 1
                pre, cur = cur, i
        return ans
