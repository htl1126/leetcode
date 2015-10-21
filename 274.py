import sys

# ref: https://leetcode.com/discuss/59615/accepted-python-solution-36ms

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        num_cite = len(citations)
        if num_cite == 0:
            return 0
        count = [0] * num_cite
        for cite in citations:
            if cite >= num_cite:
                count[num_cite - 1] += 1
            elif cite > 0:
                count[cite - 1] += 1
        h = 0
        for i in xrange(num_cite - 1, -1, -1):
            h += count[i]
            if h >= i + 1:
                return min(h, i + 1) # in case input is [0]
        return h

if __name__ == '__main__':
    sol = Solution()
    index_lst = [int(i) for i in sys.argv[1].split(',')]
    print sol.hIndex(index_lst)
