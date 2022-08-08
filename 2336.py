# Ref: https://leetcode.com/problems/smallest-number-in-infinite-set/discuss/2265333/Set-and-Counter

class SmallestInfiniteSet:

    def __init__(self):
        self.cur = 1
        self.added = set()

    def popSmallest(self) -> int:
        if len(self.added):
            ans = min(self.added)
            self.added.remove(ans)
            return ans
        self.cur += 1
        return self.cur - 1

    def addBack(self, num: int) -> None:
        if num < self.cur:
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
