# Ref: https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions

import heapq
import collections

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        q, visited, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in visited:
                visited[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time + w, v))
        return max(visited.values()) if len(visited) == N else -1

if __name__ == "__main__":
    sol = Solution()
    print sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
