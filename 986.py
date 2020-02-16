# Ref: https://leetcode.com/problems/interval-list-intersections/discuss/231100/Python-short-O(m%2Bn)-solution

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j, res = 0, 0, []
        while i < len(A) and j < len(B):
            intersect_x, intersect_y = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
            if intersect_x <= intersect_y:
                res += [[intersect_x, intersect_y]]
            if A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])
