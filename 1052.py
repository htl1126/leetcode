# Ref: https://leetcode.com/problems/grumpy-bookstore-owner/discuss/299230/JavaPython-3-Sliding-window.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        non_grumpy_sum = grumpy_sum = max_grumpy_sum = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                non_grumpy_sum += customers[i]
            else:
                grumpy_sum += customers[i]
            if i - minutes >= 0 and grumpy[i - minutes] == 1:
                grumpy_sum -= customers[i - minutes]
            max_grumpy_sum = max(max_grumpy_sum, grumpy_sum)
        return non_grumpy_sum + max_grumpy_sum
