# Ref: https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood

import collections

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        for x in nums:
            step = collections.defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[target]

if __name__ == "__main__":
    sol = Solution()
    print sol.findTargetSumWays([1, 1, 1, 1, 1], 3)
