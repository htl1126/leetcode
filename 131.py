# ref: https://leetcode.com/discuss/51759/share-my-dynamic-programming
#              solution-with-explaination


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        ans = {0: [[]], 1: [[s[0]]]}
        for i in xrange(1, len(s)):
            ans[i + 1] = []
            for j in xrange(i + 1):
                if self.isPalindrome(s[j:i + 1]):
                    for sol in ans[j]:
                        ans[i + 1].append(sol + [s[j:i + 1]])
        return ans[len(s)]

    def isPalindrome(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.partition('aab')
