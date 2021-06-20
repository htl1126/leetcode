# Ref: https://leetcode.com/problems/bus-routes/discuss/122771/C%2B%2BJavaPython-BFS-Solution

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        available_routes = collections.defaultdict(set)
        route_taken = [False] * len(routes)
        for i, route in enumerate(routes):
            for j in route:
                available_routes[j].add(i)
        bfs = [(source, 0)]
        seen = set([source])
        for stop, bus in bfs:
            if stop == target:
                return bus
            for i in available_routes[stop]:
                if not route_taken[i]:
                    for j in routes[i]:
                        if j not in seen:
                            bfs.append([j, bus + 1])
                            seen.add(j)
                    route_taken[i] = True
        return -1
