# Ref: https://leetcode.com/problems/student-attendance-record-i/discuss/101599/Java-O(N)-solution-Accepted

class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = len_l = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count_a += 1
            if s[i] == 'L':
                len_l += 1
            else:
                len_l = 0
            if count_a >= 2 or len_l >= 3:
                return False
        return True
