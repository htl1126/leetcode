# Ref: https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/discuss/709225/Most-of-the-Solutions-here-are-wrong.-Correct-solution-is-here./813904

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d, ans = collections.Counter(), 0
        for n in arr:
            if d[(-n) % k]:
                ans += 2
                d[(-n) % k] -= 1
            else:
                d[n % k] += 1
        return ans == len(arr)
