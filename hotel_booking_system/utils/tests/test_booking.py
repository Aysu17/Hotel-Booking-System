import unittest
from datetime import datetime
from models.room import Room
from models.customer import Customer
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        """This method will run before each test."""
        # Set up sample data for testing
        self.room = Room(room_number=101, room_type="Single", price_per_night=100)
        self.customer = Customer(customer_id=1, name="John Doe", email="john.doe@example.com")
        self.start_date = datetime(2024, 12, 25)
        self.end_date = datetime(2024, 12, 30)
    
    def test_booking_initialization(self):
        """Test if booking is initialized correctly."""
        booking = Booking(self.customer, self.room, self.start_date, self.end_date)
        self.assertEqual(booking.customer, self.customer)
        self.assertEqual(booking.room, self.room)
        self.assertEqual(booking.start_date, self.start_date)
        self.assertEqual(booking.end_date, self.end_date)
        self.assertEqual(booking.booking_date.date(), datetime.now().date())  # Assuming booking date is set to today

    def test_booking_str_method(self):
        """Test if the __str__ method works as expected."""
        booking = Booking(self.customer, self.room, self.start_date, self.end_date)
        expected_str = f"Booking: John Doe (john.doe@example.com) for Room 101 from 2024-12-25 00:00:00 to 2024-12-30 00:00:00"
        self.assertEqual(str(booking), expected_str)
    
    def test_booking_date_validation(self):
        """Test booking with invalid dates (end date before start date)."""
        invalid_end_date = datetime(2024, 12, 20)
        with self.assertRaises(ValueError):
            Booking(self.customer, self.room, self.start_date, invalid_end_date)
    
    def test_booking_room_availability(self):
        """Test if room is available (this will rely on the Room's availability logic)."""
        # Initially, the room should be available
        self.assertTrue(self.room.is_available)

        # Create a booking
        booking = Booking(self.customer, self.room, self.start_date, self.end_date)
        
        # After booking, the room should not be available
        self.assertFalse(self.room.is_available)

        # Release the room
        self.room.release_room()

        # After releasing, the room should be available again
        self.assertTrue(self.room.is_available)

if __name__ == "__main__":
    unittest.main()
