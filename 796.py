# Ref: https://leetcode.com/problems/rotate-string/discuss/118689/C%2B%2BJavaPython-1-line-solution

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
