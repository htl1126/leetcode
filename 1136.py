class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        queue = collections.deque([])
        
        for i, j in relations:
            suc[i].add(j)
            pre[j].add(i)
        isolated = set(list(range(1, n + 1))) - set(list(pre.keys()))
        for i in isolated:
            queue.append((1, i))
        
        order = []
        max_level = -1
        while queue:
            level, a = queue.popleft()  # must pop from left since each item has the level info
            max_level = max(max_level, level)
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    queue.append((level + 1, b))
            order.append(a)
        return max_level if len(order) == n else -1
