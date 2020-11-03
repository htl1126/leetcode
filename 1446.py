class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cur = [None, 0], [' ', 1]
        s = " " + s + " "
        for i in xrange(1, len(s)):
            if s[i - 1] != s[i]:
                if cur[1] > res[1]:
                    res = [cur[0], cur[1]]
                cur = [s[i], 0]
            cur[1] += 1
        return res[1]

if __name__ == "__main__":
    sol = Solution()
    print sol.maxPower("abbcccddddeeeeedcba")
