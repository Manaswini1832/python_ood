from parkingLot import ParkingLot
from vehicle import Vehicle, VehicleType


parking_lot = ParkingLot()

parking_lot.add_floor()
parking_lot.add_floor()

parking_lot.add_spot(1, VehicleType.BICYCLE)
parking_lot.add_spot(1, VehicleType.BICYCLE)
parking_lot.add_spot(1, VehicleType.BICYCLE)
parking_lot.add_spot(1, VehicleType.TRUCK)

parking_lot.add_spot(2, VehicleType.SCOOTY)
parking_lot.add_spot(2, VehicleType.CAR)
parking_lot.add_spot(2, VehicleType.BICYCLE)
parking_lot.add_spot(2, VehicleType.CAR)

parking_lot.floor_display(1)
parking_lot.floor_display(2)

car = Vehicle("TS01AB1234", VehicleType.CAR)

ticket = parking_lot.park_vehicle(car)

if ticket:
    parking_lot.unpark_vehicle(ticket, 5)