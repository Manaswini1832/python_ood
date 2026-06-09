class ParkingFloor:
    def __init__(self, floor_num):
        self.floor_num = floor_num

        self.spots = {
            "BICYCLE": [],
            "SCOOTY": [],
            "CAR": [],
            "TRUCK": []
        }