# Ref: https://leetcode.com/problems/stock-price-fluctuation/discuss/1513413/JavaC%2B%2BPython-Strightforward-Solutions

import sortedcontainers

class StockPrice:

    def __init__(self):
        self.time_to_price = sortedcontainers.SortedDict()
        self.price_to_time = sortedcontainers.SortedDict()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_to_price:
            prev_price = self.time_to_price[timestamp]
            self.price_to_time[prev_price].remove(timestamp)
            if len(self.price_to_time[prev_price]) == 0:
                self.price_to_time.pop(prev_price)
        if price not in self.price_to_time:
            self.price_to_time[price] = set()
        self.price_to_time[price].add(timestamp)
        self.time_to_price[timestamp] = price

    def current(self) -> int:
        return self.time_to_price.peekitem(-1)[1]

    def maximum(self) -> int:
        return self.price_to_time.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.price_to_time.peekitem(0)[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
