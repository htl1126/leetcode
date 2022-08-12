# Ref: https://leetcode.com/problems/minimum-moves-to-reach-target-score/discuss/1693327/JavaC%2B%2BPython-Reduce-target-to-1

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target > 1 and maxDoubles > 0:
            ans += 1 + target % 2
            maxDoubles -= 1
            target >>= 1
        return target - 1 + ans
