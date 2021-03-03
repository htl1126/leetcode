# Ref: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = ans = sum(cardPoints[:-k])
        for i in range(k):
            curr = curr - cardPoints[i] + cardPoints[-(k - i)]
            ans = min(ans, curr)
        return sum(cardPoints) - ans
