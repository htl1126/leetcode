# Ref: https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/431528/Python-Dijkstra-Short

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        player, box, target, empty_pos = None, None, None, set()
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == '#':
                    continue
                elif c == 'S':
                    player = i, j
                elif c == 'B':
                    box = i, j
                elif c == 'T':
                    target = i, j
                empty_pos.add((i, j))

        h, seen = [(0, *player, *box)], set()
        while h:
            m, pi, pj, bi, bj = heapq.heappop(h)
            if (bi, bj) == target: 
                return m
            if (pi, pj, bi, bj) in seen:
                continue
            seen.add((pi, pj, bi, bj))
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                new_pi, new_pj, new_bi, new_bj = pi + dx, pj + dy, bi + dx, bj + dy
                if (new_pi, new_pj) in empty_pos:
                    if (new_pi, new_pj) == (bi, bj):
                        heapq.heappush(h, (m + 1, new_pi, new_pj, new_bi, new_bj))
                    else:
                        heapq.heappush(h, (m, new_pi, new_pj, bi, bj))
        return -1
