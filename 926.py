# Ref: https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/184110/python-O(n)-time-O(1)-space-solution-with-explanation(with-extra-Chinese-explanation)

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        count_right_zero = s.count('0')
        count_left_one = 0
        ans = n - count_right_zero
        for i in range(n):
            if s[i] == '0':
                count_right_zero -= 1
            else:
                ans = min(ans, count_right_zero + count_left_one)
                count_left_one += 1
        return ans
