# ref: https://discuss.leetcode.com/topic/31561/some-python-solutions

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

if __name__ == '__main__':
    sol = Solution()
    print sol.removeDuplicateLetters('cba')
