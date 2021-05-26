# ref: https://leetcode.com/discuss/50284/12-lines-python
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # missing: the number of chars needed to for taking all the chars in t
        # need: freq of each char in the window; negative: we are having more than we need
        #                                        positive: we still need more
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:  # we have collected all the chars in t
                while i < j and need[s[i]] < 0:  # shrink the window
                    need[s[i]] += 1
                    i += 1
                if not J or j - i < J - I:  # I and J are 0's in the beginning
                    I, J = i, j
        return s[I:J]

if __name__ == '__main__':
    sol = Solution()
    print sol.minWindow('ADOBECODEBANC', 'ABC')
