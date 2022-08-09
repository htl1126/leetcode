# Ref: https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/225801/Proof-of-the-greedy-solution

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        ans, cur = 0, float('-inf')
        for l, r in pairs:
            if l > cur:
                cur = r
                ans += 1
        return ans
