class BookingService:
    def __init__(self, room_service):
        self.room_service = room_service
        self.bookings = []

    def create_booking(self, customer, room_type, start_date, end_date):
        room = self.room_service.find_available_room(room_type)
        if room:
            if room.book_room():
                booking = Booking(customer, room, start_date, end_date)
                self.bookings.append(booking)
                return booking
        return None
