from models.booking import Booking
from models.room import Room
from models.user import User
from services.emailService import send_booking_confirmation
from datetime import datetime

class BookingController:
    
    @staticmethod
    def create_booking(user_id, room_id, check_in_date, check_out_date):
        user = User.get_user_by_id(user_id)
        room = Room.get_room_by_id(room_id)
        
        # Validate room availability
        if not room.is_available(check_in_date, check_out_date):
            return "Room is not available for the selected dates."
        
        booking = Booking(user_id, room_id, check_in_date, check_out_date)
        booking.save()  # Save booking in database
        
        # Send confirmation email
        send_booking_confirmation(user.email, booking)
        
        return f"Booking confirmed for {user.name}."

    @staticmethod
    def view_booking(booking_id):
        booking = Booking.get_booking_by_id(booking_id)
        if booking:
            return booking
        return "Booking not found."

    @staticmethod
    def cancel_booking(booking_id):
        booking = Booking.get_booking_by_id(booking_id)
        if booking:
            booking.cancel()
            return "Booking canceled successfully."
        return "Booking not found."
