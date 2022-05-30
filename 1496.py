class Solution:
    def isPathCrossing(self, path: str) -> bool:
        p_set = set({(0, 0)})
        i, j = 0, 0
        d = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        for step in path:
            i, j = i + d[step][0], j + d[step][1]
            if (i, j) in p_set:
                return True
            p_set.add((i, j))
        return False
