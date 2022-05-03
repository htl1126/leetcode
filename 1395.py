# Ref: https://leetcode.com/problems/count-number-of-teams/discuss/565479/python-greater97.98-simple-logic-and-very-detailed-explanation

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i, v in enumerate(rating[1:-1]):
            llc = rgc = lgc = rlc = 0
            # v == rating[1], ..., rating[n - 2], i = 0, 1, ...
            # so l should be 0, ..., i + 1 for indexing in rating[]
            for l in range(i + 1):
                if rating[l] < v:
                    llc += 1
                elif rating[l] > v:
                    lgc += 1
            for r in range(i + 2, len(rating)):
                if rating[r] > v:
                    rgc += 1
                elif rating[r] < v:
                    rlc += 1
            ans += llc * rgc + lgc * rlc           
        return ans
