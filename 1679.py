# Ref: https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/1022699/Python-Short-Counter-solution-%2B-Oneliner-explained

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans, c = 0, collections.Counter(nums)
        for n in c:
            ans += min(c[n], c[k - n])
        return ans // 2
