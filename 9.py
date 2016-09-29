class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        s = str(x)
        length = len(s)
        is_palindrome = True
        for i in xrange(0, length / 2):
            if s[i] != s[length - 1 - i]:
                is_palindrome = False
                break
        return is_palindrome
