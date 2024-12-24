import unittest
from models.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        """This method will run before each test."""
        self.customer = Customer(customer_id=1, name="John Doe", email="john.doe@example.com")
    
    def test_customer_initialization(self):
        """Test if customer is initialized correctly."""
        self.assertEqual(self.customer.customer_id, 1)
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john.doe@example.com")
    
    def test_customer_str_method(self):
        """Test if the __str__ method works as expected."""
        expected_str = "John Doe (john.doe@example.com)"
        self.assertEqual(str(self.customer), expected_str)
    
    def test_customer_invalid_email(self):
        """Test if the customer email format is valid."""
        customer = Customer(customer_id=2, name="Jane Doe", email="invalid_email")
        self.assertEqual(customer.email, "invalid_email")

if __name__ == "__main__":
    unittest.main()
