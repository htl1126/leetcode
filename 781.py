# Ref: https://leetcode.com/problems/rabbits-in-forest/discuss/114721/C%2B%2BJavaPython-Easy-and-Concise-Solution

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = collections.Counter(answers)
        return sum((c[i] + i) // (i + 1) * (i + 1) for i in c)
