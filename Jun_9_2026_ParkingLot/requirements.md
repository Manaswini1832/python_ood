## Functional requirements of the system

1. Users should be able to request a Parking spot based on their vehicle type
2. On getting assigned a parking spot in a particular floor, they get a ticket assigned
3. While unparking their vehicle while leaving, they can scan the ticket and pay by no of hours parked
4. Each floor can have a display showing no of spots available for each vehicle type
5. Types of vehicles supported(can be improved later) : bicycle, scooty, car, truck

## Important methods/flows to explore later

1. parkVehicle()
   - ask for a parking spot
   - check floors in a first spot in queue fashion
   - if not available, show "Not available"
   - if available, assign spot to user and mark it "Parked" in that floor
   - return success

2. unparkVehicle()
   - spotId and vehicleId/licenseNo to unpark
   - call payPrice sending TicketId
   - mark spot as "Free"

3. payPrice
   - get hours parked from the ticket
   - multiply that with amounts specific to vehicle type

## Entities

1. User
2. ParkingLot
3. ParkingFloor
4. ParkingSpot
5. Ticket
6. Vehicle
