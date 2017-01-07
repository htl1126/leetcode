# ref: https://discuss.leetcode.com/topic/65991/python-o-n-solution-using-hash
#              -map


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c1, c2 = Counter(s), {}
        for k, v in c1.items():
            c2.setdefault(v, []).append(k * v)
        return ''.join([''.join(c2[i]) for i in xrange(len(s), -1, -1) if i in c2])

if __name__ == '__main__':
    sol = Solution()
    print sol.frequencySort('tree')
