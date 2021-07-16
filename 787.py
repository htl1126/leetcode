# Ref: https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = collections.defaultdict(dict)
        for a, b, w in flights:
            g[a][b] = w
        q = [(0, src, K + 1)]
        # This BFS approach guarantees that no node will be visited twice since this will lead
        # to a longer route (and a cycle)
        while q:
            p, i, k = heapq.heappop(q)
            if i == dst:
                return p
            if k >= 1:
                for j in g[i]:
                    heapq.heappush(q, (p + g[i][j], j, k - 1))
        return -1
