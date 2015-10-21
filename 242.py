import sys

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    sol = Solution()
    print sol.isAnagram(sys.argv[1], sys.argv[2])
