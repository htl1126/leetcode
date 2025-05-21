# ref: https://leetcode.com/problems/finding-3-digit-even-numbers/solutions/1612150/three-cycles

from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res, cnt = [], Counter(digits)

        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10, 2):
                    if (cnt[i] > 0 and  # freq of i > 0
                        cnt[j] > (i == j) and  # freq of j > 0 if i == j; freq of j > 1 if i != j
                        cnt[k] > (k == i) + (k == j)):  # similar to cnt[j] logic
                        res.append(i * 100 + j * 10 + k)

        return res

