# Ref: https://leetcode.com/problems/longest-happy-string/discuss/564248/Python-HEAP-solution-with-explanation

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans, h = [], []
        for count, c in ((-a, 'a'), (-b, 'b'), (-c, 'c')):
            if count:
                heapq.heappush(h, (count, c))
        while h:
            count, c = heapq.heappop(h)
            if len(ans) >= 2 and ans[-1] == ans[-2] == c:
                if not h:
                    break
                count2, c2 = heapq.heappop(h)
                heapq.heappush(h, (count, c))
                count, c = count2, c2
            ans.append(c)
            if count != -1:
                heapq.heappush(h, (count + 1, c))
        return "".join(ans)
