class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True  # Rooms are available by default

    def book_room(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def release_room(self):
        self.is_available = True
