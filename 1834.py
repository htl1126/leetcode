# Ref: https://leetcode.com/problems/single-threaded-cpu/discuss/1163980/Python-Sort-then-Heap

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        i = 0
        h = []
        n = len(tasks)
        tasks = sorted((t[0], t[1], i) for i, t in enumerate(tasks))
        t = tasks[0][0]
        while len(ans) < n:
            while i < n and tasks[i][0] <= t:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if h:
                t_diff, idx = heapq.heappop(h)
                t += t_diff
                ans.append(idx)
            else:
                t = tasks[i][0]
        return ans
