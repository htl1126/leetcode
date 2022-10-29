# Ref: https://leetcode.com/problems/process-tasks-using-servers/discuss/1239767/Python-3-Simulation-Heap-Solution

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []
        idle = [[weight, idx, 0] for idx, weight in enumerate(servers)]
        using = []
        heapq.heapify(idle)
        for t, task in enumerate(tasks):
            # using and using[0][0] <= t: get the first free server
            # not idle: directly pick a busy server and wait until it becomes free
            while using and using[0][0] <= t or not idle:
                available_t, weight, idx = heapq.heappop(using)
                heapq.heappush(idle, [weight, idx, available_t])
            weight, idx, available_t = heapq.heappop(idle)
            ans.append(idx)
            heapq.heappush(using, [max(available_t, t) + task, weight, idx])
        return ans
