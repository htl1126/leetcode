# Ref: https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/693918/Python-BFS-*-BFS-or-130ms-or-beats-95-or-Explained-and-Commented

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        player, box, target, non_obstacle = None, None, None, set()
        row, col = len(grid), len(grid[0])
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
                non_obstacle.add((i, j))

        def check(cur, dest, box):
            q = collections.deque([cur])
            seen = set(cur)
            while q:
                i, j = q.popleft()
                if (i, j) == dest:
                    return True
                for x, y in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                    if (x, y) in non_obstacle and (x, y) not in seen and (x, y) != box:
                        seen.add((x, y))
                        q.append((x, y))
            return False

        q, seen = collections.deque([(0, *player, *box)]), set(player + box)
        while q:
            m, pi, pj, bi, bj = q.popleft()
            if (bi, bj) == target:
                return m
            new_box = [(bi + 1, bj), (bi - 1, bj), (bi, bj + 1), (bi, bj - 1)]
            new_player = [(bi - 1, bj), (bi + 1, bj), (bi, bj - 1), (bi, bj + 1)]
            for new_b, new_p in zip(new_box, new_player):
                if new_b in non_obstacle and (bi, bj) + new_b not in seen:
                    if new_p in non_obstacle and check((pi, pj), new_p, (bi, bj)):
                        seen.add((bi, bj) + new_b)
                        q.append((m + 1, bi, bj, *new_b))
        return -1
