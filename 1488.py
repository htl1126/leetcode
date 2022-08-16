# Ref: https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697950/Python-well-explained-and-simple-logic-O(nlogn)-greedy-and-heap

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        dic = collections.defaultdict(collections.deque)
        ans = [-1] * len(rains)
        to_empty = []
        for day, lake in enumerate(rains):
            dic[lake].append(day)
        for i, lake in enumerate(rains):
            if lake:
                if lake in dic and dic[lake][0] < i:  # the lake is already full before day i
                    return []
                if lake in dic and len(dic[lake]) > 1:  # the lake might be flooded in the future
                    heapq.heappush(to_empty, dic[lake][1])  # push the future day that the lake might get flooded
            else:
                if to_empty:
                    ans[i] = rains[heapq.heappop(to_empty)]
                    dic[ans[i]].popleft()  # lake ans[i] poured on day dic[ans[i]][0] is dried, so we remove it
                else:
                    ans[i] = 1  # no lakes to be dried, just set the value to day 1
        return ans
