class Ticket:
    ticket_counter = 1

    def __init__(self, vehicle, entry_time, spot):
        self.id = Ticket.ticket_counter
        Ticket.ticket_counter += 1

        self.vehicle = vehicle
        self.entry_time = entry_time
        self.spot = spot

    def __str__(self):
        return f"Ticket #{self.id} - {self.vehicle.license_no}"