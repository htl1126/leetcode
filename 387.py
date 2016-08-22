import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ctr = collections.OrderedDict()
        for i, c in enumerate(s):
            if c in ctr:
                ctr[c] += i,
            else:
                ctr[c] = [i]
        for c in ctr:
            if len(ctr[c]) == 1:
                return ctr[c][0]
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.firstUniqChar('loveleetcode')
