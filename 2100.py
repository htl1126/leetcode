# Ref: https://leetcode.com/problems/find-good-days-to-rob-the-bank/discuss/1623415/Python-Explanation-with-pictures-prefix-sum.

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return list(range(n))

        left, right = [1], [1]
        cur = 1
        for i in range(1, n):
            cur = cur + 1 if security[i - 1] >= security[i] else 1
            left.append(cur)
        cur = 1
        for i in range(n - 2, -1, -1):
            cur = cur + 1 if security[i] <= security[i + 1] else 1
            right.append(cur)
        right.reverse()
        
        return [i for i in range(n) if left[i] >= time + 1 and right[i] >= time + 1]
