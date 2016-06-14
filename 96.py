# ref: https://leetcode.com/discuss/24282/dp-solution-in-6-lines-with
#              -explanation-f-i-n-g-i-1-g-n-i


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [1 for _ in xrange(n + 1)]
        for i in xrange(2, n + 1):
            G[i] = 0
            for j in xrange(i / 2):
                G[i] += G[j] * G[i - j - 1]
            G[i] <<= 1
            if i % 2 == 1:
                G[i] += G[i / 2] ** 2
        return G[n]

if __name__ == '__main__':
    sol = Solution()
    print sol.numTrees(5)
