# producer-consumer problem, source: https://leetcode.com/discuss/73589/concise-python-code

import sys

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B, record = 0, 0, {}
        for i, s in enumerate(secret):
            g = guess[i]
            if s == g:
                A += 1
            else:
                numS, numG = record.get(s, 0), record.get(g, 0)
                record[s], record[g] = numS + 1, numG - 1
                B += (numS < 0) + (numG > 0)

        return '{0}A{1}B'.format(A, B)

if __name__ == '__main__':
    sol = Solution()
    print sol.getHint(sys.argv[1], sys.argv[2])
