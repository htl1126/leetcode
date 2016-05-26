# ref: https://leetcode.com/discuss/71914/java-and-python-solutions
#              -with-and-without-tables


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None:
            return None
        C = [[0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
        for i, row in enumerate(A):
            for k, elem_A in enumerate(row):
                if elem_A:
                    for j, elem_B in enumerate(B[k]):
                        if elem_B:
                            C[i][j] += elem_A * elem_B
        return C

if __name__ == '__main__':
    sol = Solution()
    C = sol.multiply([[1, 0, 0], [-1, 0, 3]],
                     [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
    for i in xrange(len(C)):
        print ' '.join([str(num) for num in C[i]])
