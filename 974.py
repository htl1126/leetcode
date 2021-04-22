# Ref: https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217985/JavaC%2B%2BPython-Prefix-Sum

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        prefix = 0
        count = [1] + [0] * (K - 1)
        for a in A:
            prefix = (prefix + a) % K
            ans += count[prefix]
            count[prefix] += 1
        return ans
