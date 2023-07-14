# Ref: https://leetcode.com/problems/time-needed-to-buy-tickets/solutions/1576932/c-one-pass/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(len(tickets)):
            ans += min(tickets[k] - (i > k), tickets[i])
        return ans
