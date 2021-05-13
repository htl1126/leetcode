# Ref: https://leetcode.com/problems/max-value-of-equation/discuss/709231/JavaPython-Priority-Queue-and-Deque-Solution-O(N)

# O(nlogn) solution
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q, ans = [], float('-inf')
        for x, y in points:
            while q and x - q[0][1] > k:
                heapq.heappop(q)
            if q:
                ans = max(ans, -q[0][0] + x + y)
            heapq.heappush(q, (x - y, x))
        return ans

# O(n) solution
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q, ans = collections.deque(), float('-inf')
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                ans = max(ans, q[0][0] + x + y)
            while q and q[-1][0] <= y - x:
                q.pop()
            q.append([y - x, x])
        return ans
