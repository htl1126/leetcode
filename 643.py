class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur, ans = 0, float('-inf')
        for i, n in enumerate(nums):
            cur += n
            if i >= k:
                cur -= nums[i - k]
            if i >= k - 1:
                ans = max(ans, cur)
        return ans / k
