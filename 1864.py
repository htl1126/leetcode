# Ref: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/discuss/1211155/Count-Misplaced-Chars

class Solution:
    def minSwaps(self, s: str) -> int:
        count_0 = s.count('0')
        count_1 = len(s) - count_0
        if abs(count_0 - count_1) > 1:
            return -1

        tobeplaced_0 = tobeplaced_1 = 0
        for i in range(0, len(s), 2):
            if s[i] == '0':
                tobeplaced_0 += 1
            else:
                tobeplaced_1 += 1

        if count_0 == count_1:
            return min(tobeplaced_0, tobeplaced_1)
        else:
            if count_0 > count_1:
                return tobeplaced_1
            else:
                return tobeplaced_0
