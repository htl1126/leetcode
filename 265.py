# ref: https://discuss.leetcode.com/topic/22580/ac-java-solution-without-extra
#              -space/2


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n, k = len(costs), len(costs[0])
        min1, min2 = -1, -1
        for i in xrange(n):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            for j in xrange(k):
                if j != last1:
                    if last1 >= 0:
                        costs[i][j] += costs[i - 1][last1]
                else:
                    if last2 >= 0:
                        costs[i][j] += costs[i - 1][last2]
                if min1 < 0 or costs[i][j] < costs[i][min1]:
                    min2, min1 = min1, j
                elif min2 < 0 or costs[i][j] < costs[i][min2]:
                    min2 = j
        return costs[n - 1][min1]

if __name__ == '__main__':
    sol = Solution()
    print sol.minCostII()
