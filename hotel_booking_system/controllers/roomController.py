from models.room import Room
from services.emailService import send_room_update_notification

class RoomController:
    
    @staticmethod
    def add_room(room_type, price, availability, description):
        room = Room(room_type, price, availability, description)
        room.save()  # Save room to database
        return f"Room {room.room_type} added successfully."

    @staticmethod
    def edit_room(room_id, new_price=None, new_availability=None, new_description=None):
        room = Room.get_room_by_id(room_id)
        if room:
            room.update(new_price, new_availability, new_description)
            send_room_update_notification(room)
            return f"Room {room.room_type} updated successfully."
        return "Room not found."
    
    @staticmethod
    def view_room(room_id):
        room = Room.get_room_by_id(room_id)
        if room:
            return room
        return "Room not found."
    
    @staticmethod
    def list_rooms():
        rooms = Room.get_all_rooms()
        return rooms
