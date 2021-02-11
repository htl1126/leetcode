class UndergroundSystem:

    def __init__(self):
        self.checkin = collections.defaultdict(lambda: ["", 0])
        self.dis = collections.defaultdict(lambda: [])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.dis[(self.checkin[id][0], stationName)].append(t - self.checkin[id][1])
        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.dis[(startStation, endStation)]) / len(self.dis[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
