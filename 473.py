# Ref: https://leetcode.com/problems/matchsticks-to-square/discuss/1273708/Python-dp-on-subsets-explained
# This is a special case of Problem 698

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sums = [0] * 4
        subsum = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        def walk(i):
            if i == len(matchsticks):
                return len(set(sums)) == 1
            for j in range(4):
                sums[j] += matchsticks[i]
                if sums[j] <= subsum and walk(i + 1):
                    return True
                sums[j] -= matchsticks[i]
                if sums[j] == 0:
                    break
            return False

        return walk(0)
