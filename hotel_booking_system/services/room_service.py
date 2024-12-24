class RoomService:
    def __init__(self, rooms):
        self.rooms = rooms

    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.room_type == room_type and room.is_available:
                return room
        return None

    def add_room(self, room):
        self.rooms.append(room)
