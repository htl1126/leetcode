import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        row, col, ans = len(heightMap), len(heightMap[0]), 0
        visited = [[False] * col for _ in xrange(row)]
        outer = [(i, j) for k in xrange(max(row, col)) for (i, j) in
                 (0, k), (row - 1, k), (k, 0), (k, col - 1)]
        heap = []
        for i, j in outer:
            if 0 <= i < row and 0 <= j < col:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        while heap:
            h, i, j = heapq.heappop(heap)
            for I, J in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                if 0 <= I < row and 0 <= J < col and not visited[I][J]:
                    heapq.heappush(heap, (max(h, heightMap[I][J]), I, J))
                    ans += max(0, h - heightMap[I][J])
                    visited[I][J] = True
        return ans
