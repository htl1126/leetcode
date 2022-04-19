# Ref: https://leetcode.com/problems/count-square-sum-triples/discuss/1540448/Python-simple-solution

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                s = math.sqrt(i * i + j * j)
                if int(s) == s and s <= n:
                    ans += 2
        return ans
