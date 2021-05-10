# Ref: https://leetcode.com/problems/time-based-key-value-store/discuss/227943/Python-Dict-and-Binary-search-Implementation

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        a = self.data[key]
        l, r = 0, len(a)
        while l < r:
            m = (l + r) // 2
            if a[m][0] <= timestamp:
                l = m + 1
            else:
                r = m
        return "" if l == 0 else a[l - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
