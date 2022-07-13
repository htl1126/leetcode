# Ref: https://leetcode.com/problems/sequentially-ordinal-rank-tracker/discuss/1623292/Python-SortedList-No-Need-to-Think-Explain-behind-the-scene!-O(logN)

import sortedcontainers

class SORTracker:

    def __init__(self):
        self.sorted_list = sortedcontainers.SortedList()
        self.i = 0

    def add(self, name: str, score: int) -> None:
        self.sorted_list.add([-score, name])

    def get(self) -> str:
        s = self.sorted_list[self.i][1]
        self.i += 1
        return s


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
