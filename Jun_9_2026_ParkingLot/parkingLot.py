from parkingFloor import ParkingFloor
from parkingSpot import ParkingSpot
from vehicle import VehicleType
from ticket import Ticket


class ParkingLot:
    def __init__(self):
        self.num_floors = 0
        self.floors = []
        self.tickets = []

    def add_floor(self):
        floor = ParkingFloor(self.num_floors + 1)

        self.floors.append(floor)
        self.num_floors += 1

    def add_spot(self, floor_num, vehicle_type):
        spot = ParkingSpot(vehicle_type)

        self.floors[floor_num - 1].spots[
            vehicle_type.name
        ].append(spot)

    def floor_display(self, floor_num):
        floor = self.floors[floor_num - 1]

        print(f"\nFloor {floor_num}")

        for vehicle_type, spots in floor.spots.items():
            print(
                f"{vehicle_type}: "
                f"{len(spots)} spots"
            )

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spots = floor.spots[vehicle.type.name]

            for spot in spots:
                if not spot.is_occupied:
                    spot.is_occupied = True
                    spot.vehicle = vehicle

                    ticket = Ticket(
                        vehicle,
                        entry_time=0,
                        spot=spot
                    )

                    self.tickets.append(ticket)

                    print(
                        f"Vehicle parked. "
                        f"Ticket ID = {ticket.id}"
                    )

                    return ticket

        print("No spot available")
        return None

    def calculate_price(self, hours, vehicle_type):
        rates = {
            VehicleType.BICYCLE: 10,
            VehicleType.SCOOTY: 20,
            VehicleType.CAR: 50,
            VehicleType.TRUCK: 100
        }

        return rates[vehicle_type] * hours

    def unpark_vehicle(self, ticket, hours):
        ticket.spot.is_occupied = False
        ticket.spot.vehicle = None

        price = self.calculate_price(
            hours,
            ticket.vehicle.type
        )

        print(
            f"Vehicle {ticket.vehicle.license_no} "
            f"unparked."
        )

        print(f"Please pay Rs.{price}")