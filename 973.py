import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for (x, y) in points:
            dist = - (x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x, y) for (dist, x, y) in heap]

if __name__ == "__main__":
    sol = Solution()
    print sol.kClosest([[1,3],[-2,2]], 1)

# Algorithm: heap
# Ref: https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/
