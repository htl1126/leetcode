# ref: https://leetcode.com/discuss/78044/clean-python-solution-one-pass
# DP solution


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        acc, ans = 0, 0
        d = {0: -1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in d:  # only keep the "acc" value for the smallest i
                d[acc] = i
            if acc - k in d:
                ans = max(ans, i - d[acc - k])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.maxSubArrayLen([1, -1, 5, -2, 3], 3)
