class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while s[start] == s[end]:
            start += 1
            end -= 1
            if start > end:
                return True
        left, right = s[start:end], s[start + 1:end + 1]
        return left == left[::-1] or right == right[::-1]
        
if __name__ == "__main__":
    sol = Solution()
    print sol.validPalindrome("adcfa")

# algorithm: ad-hoc
# ref: https://leetcode.com/problems/valid-palindrome-ii/discuss/107718