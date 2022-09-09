class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        open_spots = self.spaces[carType]
        if open_spots > 0:
            self.spaces[carType] -= 1
            return True
        else:
            return False
            
                
obj = ParkingSystem(1, 1, 0)
obj.addCar(1)
obj.addCar(2)
obj.addCar(3)
obj.addCar(1)