# ref: https://discuss.leetcode.com/topic/49022/greedy-solution-beats-95
import collections


class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if not str or not k:
            return str
        nBin = (len(str) - 1) / k + 1
        lastBinSize = len(str) % k
        size_lst = [k] * (nBin - 1) + [lastBinSize if lastBinSize else k]
        bins = ['' for _ in xrange(nBin)]
        ctr = collections.Counter(str)
        cur = 0
        for c, count in sorted(ctr.items(), key=lambda x: -x[1]):
            if count > nBin:
                return ''
            for i in xrange(count):
                while len(bins[cur]) >= size_lst[cur]:
                    cur = (cur + 1) % nBin
                if c in bins[cur]:
                    return ''
                bins[cur] += c
                cur = (cur + 1) % nBin
        return ''.join(bins)

if __name__ == '__main__':
    sol = Solution()
    print sol.rearrangeString('abeabac', 3)
