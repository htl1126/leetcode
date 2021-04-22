# Ref: https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last7, last30, cost = collections.deque(), collections.deque(), 0
        for day in days:
            while last7 and day - last7[0][0] >= 7:
                last7.popleft()
            last7.append([day, cost + costs[1]])
            while last30 and day - last30[0][0] >= 30:
                last30.popleft()
            last30.append([day, cost + costs[2]])
            cost = min(cost + costs[0], last7[0][1], last30[0][1])
        return cost
