# Ref: https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/discuss/1375390/Python-Solution-with-detailed-explanation-and-proof-and-common-failure-analysis

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sum_milestone, max_milestone = sum(milestones), max(milestones)
        if sum_milestone - max_milestone >= max_milestone:
            return sum_milestone
        return 2 * (sum_milestone - max_milestone) + 1
