# ref: https://leetcode.com/discuss/50284/12-lines-python
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # missing: the number of chars needed to for taking all the chars in t
        # need: freq of each char in the window; negative: we are having more than we need
        #                                        positive: we still need more
        need, missing = collections.Counter(t), len(t)
        i, I, J = 0, 0, 0
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:  # we have collected all the chars in t
                while i <= j and need[s[i]] < 0:  # shrink the window
                    need[s[i]] += 1
                    i += 1
                if J == 0 or j - i < J - I:  # I and J are 0's in the beginning
                    I, J = i, j
        return s[I:J]

if __name__ == '__main__':
    sol = Solution()
    print sol.minWindow('ADOBECODEBANC', 'ABC')
