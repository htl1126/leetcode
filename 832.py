# Ref: https://leetcode.com/problems/flipping-an-image/discuss/130590/C%2B%2BJavaPython-Reverse-and-Toggle

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 ^ i for i in reversed(row)] for row in A]

if __name__ == "__main__":
    sol = Solution()
    print sol.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
