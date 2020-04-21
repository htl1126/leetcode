# Ref: https://leetcode.com/problems/sort-array-by-parity/discuss/170734/C%2B%2BJava-In-Place-Swap

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        last_even = 0
        for i in xrange(0, len(A)):
            if A[i] % 2 == 0:
                A[last_even], A[i] = A[i], A[last_even]
                last_even += 1
        return A
        
if __name__ == "__main__":
    sol = Solution()
    print sol.sortArrayByParity([0, 1, 2])
