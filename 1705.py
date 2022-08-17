# Ref: https://leetcode.com/problems/maximum-number-of-eaten-apples/discuss/988209/Easy-Python-Solution-with-Explanation-ACCEPTED

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = i = 0
        q = []
        while i < len(apples) or q:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(q, [i + days[i], apples[i]])
            while q and (q[0][0] <= i or q[0][1] == 0):  # pop when the first pile of apples are fully consumed or rotten
                heapq.heappop(q)
            if q:  # eat one apple
                q[0][1] -= 1
                ans += 1
            i += 1
        return ans
