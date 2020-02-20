# Ref: https://leetcode.com/problems/snakes-and-ladders/discuss/173663/Python-BFS-solution
# Algo: BFS

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        arr, num_grid, queue, seen, moves = [0], len(board) ** 2, [1], set(), 0
        for i, row in enumerate(board[::-1]):
            arr += row if i % 2 == 0 else row[::-1]
        while queue:
            new = []
            for s in queue:
                if s == num_grid:
                    return moves
                for i in xrange(1, 7):
                    if s + i <= num_grid and s + i not in seen:
                        seen.add(s + i)
                        new.append(s + i if arr[s + i] == -1 else arr[s + i])
            queue, moves = new, moves + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]])
