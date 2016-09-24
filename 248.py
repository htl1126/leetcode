# ref: https://discuss.leetcode.com/topic/21675/python-solution-180ms


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        a, b = self.below(high), self.below(low, include=False)
        return a - b if a > b else 0

    def below(self, n, include=True):
        res = 0
        for i in xrange(1, len(n)):
            res += self.number(i)
        l = self.strobogrammatic(len(n))
        if include:
            tmp = [num for num in l if num <= n]
        else:
            tmp = [num for num in l if num < n]
        return res + len(tmp)

    def strobogrammatic(self, n):
        return self.helper(n, n)

    def helper(self, m, n):
        if m == 0:
            return ['']
        if m == 1:
            return ['0', '1', '8']
        l = self.helper(m - 2, n)
        return [a + i + b for a, b in ['00', '11', '69', '88', '96'][m == n:]
                for i in l]

    def number(self, l):
        if l == 1:
            return 3
        elif l % 2 == 0:
            return 4 * 5 ** (l / 2 - 1)
        else:
            return 3 * 5 ** (l / 2 - 1) * 4

if __name__ == '__main__':
    sol = Solution()
    print sol.strobogrammaticInRange('50', '100')
