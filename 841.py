class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i, key_list in enumerate(rooms):
            graph[i] = key_list
        visited = [False] * len(rooms)
        def dfs(i):
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    dfs(j)
        dfs(0)
        return sum(visited) == len(visited)
