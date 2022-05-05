# Ref: https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999125/JavaPython-3-Sort-by-the-units-then-apply-greedy-algorithm.

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for count, size in boxTypes:
            if count < truckSize:
                truckSize -= count
                ans += count * size
            else:
                ans += truckSize * size
                break
        return ans
