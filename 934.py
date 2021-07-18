# ref: https://leetcode.com/problems/shortest-bridge/discuss/189440/Python-concise-DFS-and-BFS-in-1-solution

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])
        start = set()
        
        def dfs(i, j):
            A[i][j] = 2
            for x, y in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= x < r and 0 <= y < c:
                    if A[x][y] == 1:
                        dfs(x, y)
                    if A[x][y] == 0:
                        start.add((0, i, j))
                        
        def find_first_land():
            for i in range(r):
                for j in range(c):
                    if A[i][j] == 1:
                        return i, j
                    
        start_i, start_j = find_first_land()
        dfs(start_i, start_j)
        queue = list(start)
        for step, i, j in queue:
            for x, y in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= x < r and 0 <= y < c:
                    if A[x][y] == 1:
                        return step
                    elif A[x][y] == 0:
                        A[x][y] = -1  # important step to reduce the search space
                        queue.append((step + 1, x, y))
