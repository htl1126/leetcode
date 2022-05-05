class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lot = {1: 0, 2: 0, 3: 0}
        self.lot_size = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.lot[carType] < self.lot_size[carType]:
            self.lot[carType] += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
