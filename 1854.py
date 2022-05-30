# Ref: https://leetcode.com/problems/maximum-population-year/discuss/1199494/Python-sorting-max-overlapping-segments-algorithm

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        data = []
        for i, j in logs:
            data.append([i, 1])
            data.append([j, -1])
        data.sort()
        max_p = cur_p = ans = 0
        for year, i in data:
            cur_p += i
            if cur_p > max_p:
                max_p = cur_p
                ans = year
        return ans
