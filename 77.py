# ref: https://discuss.leetcode.com/topic/14626/1-liner-3-liner-4-liner


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        return [pre + [i] for i in xrange(1, n + 1)
                for pre in self.combine(i - 1, k - 1)]

if __name__ == '__main__':
    sol = Solution()
    print sol.combine(4, 2)
