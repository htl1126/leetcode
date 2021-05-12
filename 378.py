# ref: https://discuss.leetcode.com/topic/52915/shortest-possible-solution-in-python-seriously
# ref: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85219/Python-solution-O(klogk)-similar-to-problem-373
import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap, ans, n = [(matrix[0][0], 0, 0)], 0, len(matrix)
        for _ in xrange(k):
            ans, i, j = heapq.heappop(heap)
            if not i and j < n - 1:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i < n - 1:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.kthSmallest([[1,  5,  9],
                           [10, 11, 13],
                           [12, 13, 15]], 8)
