class ParkingSpot:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.is_occupied = False
        self.vehicle = None

    def __str__(self):
        status = "Occupied" if self.is_occupied else "Free"
        return f"{self.vehicle_type.name} - {status}"