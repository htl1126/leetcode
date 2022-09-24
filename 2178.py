# Ref: https://leetcode.com/problems/maximum-split-of-positive-even-integers/discuss/1783317/JavaPython-3-Greedy-w-brief-explanation-and-analysis.

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans, t = [], 2
        if finalSum % 2 == 0:
            while t <= finalSum:
                ans.append(t)
                finalSum -= t
                t += 2
            ans[-1] += finalSum
        return ans
