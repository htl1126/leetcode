import collections

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-(c + d)] for c in C for d in D)

if __name__ == "__main__"
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    sol = Solution()
    print sol.fourSumCount(A, B, C, D)

# Algorithm: Brute force
# Ref: https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
# Line 12 computes the frequency of sums "a + b" for a in A and for b in B
# Line 13 computes the sum of all the occurrences where a + b + c + d = 0
#     For example, AB[-(-1 + 2)] = 1, so we have one solution:
#                  (a, b, c, d) = (1, -2, -1, 2)
