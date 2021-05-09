# Ref: https://leetcode.com/problems/random-pick-index/discuss/88153/Python-reservoir-sampling-solution.
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans, count = None, 0
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    ans = i
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
