# concise solution: https://leetcode.com/discuss/67225/simple-python-solution

import sys
from leetcode_util import read_list

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))
        return (C - A) * (D - B) + (G - E) * (H - F) - width * height

if __name__ == '__main__':
    sol = Solution()
    print sol.computeArea(read_list(sys.argv[1])[0],
                          read_list(sys.argv[1])[1],
                          read_list(sys.argv[1])[2],
                          read_list(sys.argv[1])[3],
                          read_list(sys.argv[1])[4],
                          read_list(sys.argv[1])[5],
                          read_list(sys.argv[1])[6],
                          read_list(sys.argv[1])[7])
