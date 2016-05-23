class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cmap = {}
        for i in xrange(len(s)):
            if s[i] not in cmap:
                if t[i] not in cmap.values():
                    cmap[s[i]] = t[i]
                else:
                    return False
            else:
                if cmap[s[i]] != t[i]:
                    return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isIsomorphic('ab', 'aa')
