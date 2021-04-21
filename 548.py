# Ref: https://leetcode.com/problems/split-array-with-equal-sum/discuss/101495/5-lines-simple-Python

class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        s = [0] * (n + 1)
        # s[n] = nums[0] + nums[1] + ... + nums[n - 1]
        for i in range(n):
            s[i + 1] = s[i] + nums[i]
        def check(l, r):
            # s[m] - s[l] = nums[l] + nums[l + 1] + ... + nums[m - 1]
            # s[r + 1] - s[m + 1] = nums[m + 1] + nums[m + 2] + ... + nums[r]
            return set(s[m] - s[l] for m in range(l + 1, r) if s[m] - s[l] == s[r + 1] - s[m + 1])
        return any(check(0, j - 1) & check(j + 1, n - 1) for j in range(n))
