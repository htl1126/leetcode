# ref: https://discuss.leetcode.com/topic/7144/python-o-n-2-method-with-some
#              -optimization-88ms


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen, start = 1, 0
        for i in range(1, len(s)):
            if i - maxlen - 1 >= 0 and s[i - maxlen - 1:i + 1] == s[i - maxlen - 1:i + 1][::-1]:
                start = i - maxlen - 1
                maxlen += 2
            if i - maxlen >= 0 and s[i - maxlen:i + 1] == s[i - maxlen:i + 1][::-1]:
                start = i - maxlen
                maxlen += 1
        return s[start:start + maxlen]

if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome('aaabccb')
