import unittest
from models.room import Room

class TestRoom(unittest.TestCase):
    def test_room_booking(self):
        room = Room(101, "Single", 100)
        self.assertTrue(room.book_room())  # Should succeed
        self.assertFalse(room.is_available)  # Room should no longer be available
        room.release_room()  # Release the room
        self.assertTrue(room.is_available)  # Room should be available again

if __name__ == "__main__":
    unittest.main()
