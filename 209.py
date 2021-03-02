# ref: https://discuss.leetcode.com/topic/14288/python-o-n-and-o-n
#              -log-n-solution

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur, i, ans = 0, 0, len(nums) + 1
        for j in range(len(nums)):
            cur += nums[j]
            while cur >= target:
                ans = min(ans, j - i + 1)
                cur -= nums[i]
                i += 1
        return ans % (len(nums) + 1)

if __name__ == '__main__':
    sol = Solution()
    print sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
