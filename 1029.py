# Ref: https://leetcode.com/problems/two-city-scheduling/discuss/278800/One-line-Python
# Algo: greedy

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        return sum([x[0] for x in costs[:len(costs) / 2]] + [x[1] for x in costs[len(costs) / 2:]])

if __name__ == "__main__":
    sol = Solution()
    print sol.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
