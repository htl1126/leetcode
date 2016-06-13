# ref: https://leetcode.com/discuss/8527/dp-solution-java-for-reference


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        table = [0 for _ in xrange(len(s) + 1)]
        table[len(s)] = 1
        if s[-1] == '0':
            table[-2] = 0
        else:
            table[-2] = 1
        for i in xrange(len(s) - 2, -1, -1):
            if s[i] != '0':
                if int(s[i: i + 2]) <= 26:
                    table[i] = table[i + 1] + table[i + 2]
                else:
                    table[i] = table[i + 1]
        return table[0]

if __name__ == '__main__':
    sol = Solution()
    print sol.numDecodings('12')
