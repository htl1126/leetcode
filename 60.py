# ref: https://discuss.leetcode.com/topic/37333/python-i-think-this-is-clean
#              -code-with-some-of-my-explanation


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = map(str, range(1, n + 1))
        k -= 1
        factor = 1
        for i in xrange(1, n):
            factor *= i
        res = []
        for i in xrange(n - 1, -1, -1):
            res.append(num[k / factor])
            num.remove(num[k / factor])
            if i:
                k %= factor
                factor /= i
        return ''.join(res)

if __name__ == '__main__':
    sol = Solution()
    print sol.getPermutation(4, 18)
