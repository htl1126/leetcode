# Ref: https://leetcode.com/problems/task-scheduler/discuss/760266/Python-4-lines-linear-solution-detailed-explanation

import collections

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (n + 1) * (M - 1) + Mct)

if __name__ == "__main__":
    sol = Solution()
    # A B B C C C, N = 1
    # CBACBC
    # M = 3
    # Mct = 1
    # N = 1
    # (M - 1) * (N + 1) + Mct < num(tasks) => ans = num(tasks)
    print sol.leastInterval(["A", "A", "A", "B", "B", "C"], 1)

    # B B C C C, N = 1
    # CBCBC
    # M = 3
    # Mct = 1
    # N = 1
    # (M - 1) * (N + 1) + Mct = num(tasks) => ans = (M - 1) * (N + 1) + Mct
    print sol.leastInterval(["B", "B", "C", "C", "C"], 1)

# Algorithm: math
# Ref: https://leetcode.com/problems/task-scheduler/discuss/104507


# Solution 2
# ref: https://leetcode.com/problems/task-scheduler/discuss/130786/Python-solution-with-detailed-explanation

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr_time, h = 0, []
        for task, freq in collections.Counter(tasks).items():
            heappush(h, (-freq, task))
        while h:
            i, temp = 0, []
            # for every subwindow of size n, we want to place as many task as possible, and
            # pick higher frequent tasks first
            while i <= n:
                curr_time += 1
                if h:
                    neg_freq, task = heapq.heappop(h)
                    if neg_freq != -1:
                        temp.append((neg_freq + 1, task))
                if not h and not temp:
                    break
                i += 1
            for item in temp:
                heapq.heappush(h, item)
        return curr_time