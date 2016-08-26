# ref: https://discuss.leetcode.com/topic/48930/any-accepted-python-solution
import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def maxSumSublist(vals):
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for val in vals:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum
        maxSum = float('-inf')
        columns = zip(*matrix)
        for left in xrange(len(columns)):
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                rowSums = map(int.__add__, rowSums, column)
                maxSum = max(maxSum, maxSumSublist(rowSums))
        return maxSum

if __name__ == '__main__':
    sol = Solution()
    print sol.maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5],
                               [5, 1, 5, -4]], 8)
