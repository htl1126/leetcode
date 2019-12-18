class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if A[0] > A[-1]:
            A = A[::-1]
        for i in xrange(len(A) - 1):
            if A[i] > A[i + 1]:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isMonotonic([3, 2, 2, 1])