from enum import Enum

class VehicleType(Enum):
    BICYCLE = 1
    SCOOTY = 2
    CAR = 3
    TRUCK = 4

class Vehicle:
    def __init__(self, licenseNo, vehicle_type):
        self.license_no = licenseNo
        self.type = vehicle_type