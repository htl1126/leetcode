# Ref: https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/discuss/398342/Python-simple-oddeven-approach-with-explanation.

class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd_pos_sum = even_pos_sum = 0
        for n in position:
            if n % 2 == 1:
                odd_pos_sum += 1
            else:
                even_pos_sum += 1
        return min(odd_pos_sum, even_pos_sum)

if __name__ == '__main__':
    sol = Solution()
    print sol.minCostToMoveChips([2, 2, 2, 3, 3])
