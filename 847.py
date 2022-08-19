# Ref: https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/147123/Python-8-lines-Heapq-and-BFS-and-Deque-solutions

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        seen, step = set(), 0
        final, q = (1 << len(graph)) - 1, [(i, 1 << i) for i in range(len(graph))]
        while q:
            new_q = []
            for node, state in q:
                if state == final:
                    return step
                for v in graph[node]:
                    new_state = state | (1 << v)  # nodes can be revisited
                    if (v, new_state) not in seen:
                        seen.add((v, new_state))
                        new_q.append((v, new_state))
            q = new_q
            step += 1
