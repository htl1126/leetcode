# Ref: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/1445198/Python-Sort

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))  # notice the lambda func
        ans = curr_max = 0
        for _, y in properties:
            if y < curr_max:
                ans += 1
            else:
                curr_max = y
        return ans
