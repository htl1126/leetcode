# ref: https://discuss.leetcode.com/topic/19179/6-lines-python-8-lines-ruby


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon[0])
        need = [2 ** 31] * (n - 1) + [1]
        # we do DP from the bottom to the top, from the right to the left
        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                # if need[j] > need[j + 1], we take need[j + 1]
                # if HP won't be lost here, we set need[j] to 1
                need[j] = max(min(need[j:j + 2]) - row[j], 1)
        return need[0]

if __name__ == '__main__':
    sol = Solution()
    print sol.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
