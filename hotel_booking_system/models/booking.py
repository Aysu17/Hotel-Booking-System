from datetime import datetime

class Booking:
    def __init__(self, customer, room, start_date, end_date):
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.booking_date = datetime.now()

    def __str__(self):
        return f"Booking: {self.customer} for Room {self.room.room_number} from {self.start_date} to {self.end_date}"
