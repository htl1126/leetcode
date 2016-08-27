# ref: https://discuss.leetcode.com/topic/21337/1-lines-ruby-python


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        prev = [0] * 3
        for now in costs:
            prev = [now[i] + min(prev[:i] + prev[i + 1:]) for i in xrange(3)]
        return min(prev)

if __name__ == '__main__':
    sol = Solution()
    print sol.minCost([[1, 2, 3], [3, 2, 1]])
