# Ref: https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/discuss/1822174/C%2B%2BPython-Short-Greedy-Solution

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        ans = 0
        while s:
            i = s.index(s[-1])
            # if the last char only appears once, move it to the center
            if i == len(s) - 1:
                ans += i // 2
            # otherwise, move it to the beginning position
            else:
                ans += i
                s.pop(i)
            s.pop()
        return ans
