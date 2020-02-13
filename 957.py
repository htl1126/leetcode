# Ref: https://leetcode.com/problems/prison-cells-after-n-days/discuss/234272/Very-easy-Python-Solution
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N > 14:
            N %= 14
        if N == 0:
            N = 14
        size = len(cells)

        for _ in xrange(N):
            temp = [0 for _ in xrange(size)]
            for i in xrange(size):
                if 0 < i < size - 1 and cells[i - 1] == cells[i + 1]:
                    temp[i] = 1
                else:
                    temp[i] = 0
            cells = temp
        return cells

if __name__ == "__main__":
    sol = Solution()
    print sol.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7)
