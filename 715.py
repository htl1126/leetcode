# Ref: https://leetcode.com/problems/range-module/discuss/108913/Python

class RangeModule:

    def __init__(self):
        self.X = [0, 10 ** 9]
        self.track = [False, False]

    def addRange(self, left: int, right: int, track=True) -> None:
        def index(x):
            i = bisect.bisect_left(self.X, x)
            if self.X[i] != x:
                self.X.insert(i, x)
                self.track.insert(i, self.track[i - 1])
            return i
        i = index(left)
        j = index(right)
        self.X[i:j] = [left]
        self.track[i:j] = [track]

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect(self.X, left) - 1
        j = bisect.bisect_left(self.X, right)
        return all(self.track[i:j])

    def removeRange(self, left: int, right: int) -> None:
        self.addRange(left, right, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
