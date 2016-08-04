class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for i in xrange(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and \
                    haystack[i:i + len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.strStr('abcdef', 'cde')
