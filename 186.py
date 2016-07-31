# ref: https://discuss.leetcode.com/topic/35294/python-use-reverse-and-reversed


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        s.reverse()
        index = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                s[index:i] = reversed(s[index:i])
                index = i + 1
        s[index:] = reversed(s[index:])

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseWords(list('the sky is blue'))
