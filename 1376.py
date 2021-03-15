# Ref: https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532530/Python3-Easy-Python-Solution%3A-DijkstraBFSDFS

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = collections.defaultdict(list)
        for i, j in enumerate(manager):
            graph[j].append(i)
        def dfs(i):
            maxt = 0
            for j in graph[i]:
                maxt = max(maxt, dfs(j))
            return informTime[i] + maxt
        return dfs(headID)
