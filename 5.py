import sys

# ref: https://leetcode.com/discuss/55968/my-0ms-c-solution
# idea: every time we try to find a sequence of the same alphabet
#       , then we expand the sequence to find the largest palindrome
#       , then we proceed from the end of the last sequence of the same alphabet found

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        begin = 0
        strlen = len(s)
        ans = None
        while begin + max_len / 2 < strlen:
            right = begin + 1
            for right in xrange(begin + 1, strlen):
                if s[begin] != s[right]:
                    break
            if right == strlen - 1 and s[right] == s[begin]:
                right += 1
            left = begin
            begin = right
            while left > 0 and right < strlen:
                if s[left - 1] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if right - left > max_len:
                max_len = right - left
                ans = s[left:right]
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.longestPalindrome(sys.argv[1])
