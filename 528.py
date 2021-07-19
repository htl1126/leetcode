# Ref: https://leetcode.com/problems/random-pick-with-weight/discuss/154432/Very-easy-solution-based-on-uniform-sampling-with-explanation

import random

class Solution:

    def __init__(self, w: List[int]):
        self.acc_arr = w[:]
        for i in range(1, len(w)):
            self.acc_arr[i] += self.acc_arr[i - 1]
        self.acc_sum = self.acc_arr[-1]

    def pickIndex(self) -> int:
        i = random.randint(1, self.acc_sum)
        l, r = 0, len(self.acc_arr) - 1
        while l < r:
            m = (l + r) // 2
            if i > self.acc_arr[m]:
                l = m + 1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
