# ref: https://discuss.leetcode.com/topic/21086/iterative-and-recursive-python


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        todo, combis = [(n, 2, [])], []
        while todo:
            n, i, combi = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [n / i, i],
                    todo += (n / i, i, combi + [i]),
                i += 1
        return combis

if __name__ == '__main__':
    sol = Solution()
    print sol.getFactors(32)
