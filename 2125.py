class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = pre = cur = 0
        for s in bank:
            c = list(s).count('1')
            if c > 0:
                cur = c
                ans += pre * cur
                pre = cur
        return ans
