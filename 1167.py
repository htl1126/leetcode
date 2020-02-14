# Ref: https://leetcode.com/problems/minimum-cost-to-connect-sticks/discuss/365865/Python-Greedy-Solution
# Algo: Greedy
import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            merged = x + y
            heapq.heappush(sticks, merged)
            ans += merged
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.connectSticks([1, 8, 3, 5])
