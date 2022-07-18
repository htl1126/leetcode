# Ref: https://leetcode.com/problems/append-k-integers-with-minimal-sum/discuss/1823621/Python-Explanation-with-pictures/1296421

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        ans = k * (k + 1) // 2
        candidate = k + 1
        for n in sorted(set(nums)):
            if n < candidate:
                ans += candidate - n
                candidate += 1
        return ans
