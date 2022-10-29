# Ref: https://leetcode.com/problems/count-number-of-bad-pairs/discuss/2388121/Python-O(N)-solution-how-to-%22reverse%22-a-problem-to-make-it-easier-to-solve

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2

        d, good = {}, 0
        for i in range(n):
            dif = i - nums[i]
            good += d.get(dif, 0)
            d[dif] = d.get(dif, 0) + 1
        return total - good
