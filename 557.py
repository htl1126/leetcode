# Ref: https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101909/1-line-Ruby-Python

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.reverseWords("Let's take LeetCode contest")
