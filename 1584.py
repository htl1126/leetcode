# Ref: https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/Python-3-or-Min-Spanning-Tree-or-Prim's-Algorithm

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, g = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                g[i].append((d, j))
                g[j].append((d, i))
        ans, h, visited, count = 0, g[0], [False] * n, 1
        visited[0] = True
        heapq.heapify(h)
        while h:
            d, i = heapq.heappop(h)
            if not visited[i]:
                ans, visited[i], count = ans + d, True, count + 1
                for e in g[i]:
                    heapq.heappush(h, e)
            if count == n:
                break
        return ans
