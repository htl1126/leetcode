# Ref: https://leetcode.com/problems/random-pick-with-weight/discuss/154432/Very-easy-solution-based-on-uniform-sampling-with-explanation

import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.acc_arr = w[:]
        for i in xrange(1, len(w)):
            self.acc_arr[i] += self.acc_arr[i - 1]
        self.acc_sum = self.acc_arr[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        i = random.randint(1, self.acc_sum)
        left, right = 0, len(self.acc_arr) - 1
        while left != right:
            mid = (left + right) / 2
            if i > self.acc_arr[mid]:
                left = mid + 1
            else:
                right = mid
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
