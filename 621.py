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
