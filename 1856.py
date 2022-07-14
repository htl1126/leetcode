# Ref: https://leetcode.com/problems/maximum-subarray-min-product/discuss/1198718/JavaPython-Stack-keeps-index-of-elements-less-than-numsi-O(N)

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0] * n, [0] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1] + 1
            else:
                left[i] = 0
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1] - 1
            else:
                right[i] = n - 1
            stack.append(i)

        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * (pre_sum[right[i] + 1] - pre_sum[left[i]]))

        return ans % (10 ** 9 + 7)
