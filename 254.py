# ref: https://discuss.leetcode.com/topic/21086/iterative-and-recursive-python


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n / i],
                    factor(n / i, i, combi + [i], combis)
                i += 1
            return combis
        return factor(n, 2, [], [])

if __name__ == '__main__':
    sol = Solution()
    print sol.getFactors(32)
