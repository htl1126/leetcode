# Ref: https://leetcode.com/problems/longest-turbulent-subarray/discuss/222146/PythonJavaC%2B%2B-O(n)-time-O(1)-space-Simple-and-Clean-solution

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best, curlen = 0, 0
        for i in xrange(len(A)):
             if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                 curlen += 1
             elif i > 0 and A[i - 1] != A[i]:
                 curlen = 2
             else:
                 curlen = 1
             best = max(best, curlen)
        return best

if __name__ == "__main__":
    sol = Solution()
    print sol.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
