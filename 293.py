class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        for i in xrange(len(s) - 1):
            if s[i:i + 2] == '++':
                ans.append('{0}--{1}'.format(s[:i], s[i + 2:]))
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.generatePossibleNextMoves('++++')
