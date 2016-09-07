import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ctr = collections.Counter(s)
        return len([v for v in ctr.values() if v & 1]) <= 1

if __name__ == '__main__':
    sol = Solution()
    print sol.canPermutePalindrome('carerac')
