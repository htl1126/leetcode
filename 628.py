# Ref: https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/104739/Python-O(N)-and-1-line
# Algo: math

import heapq

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])

if __name__ == "__main__":
    sol = Solution()
    print sol.maximumProduct([1, 2, 3, 4])
