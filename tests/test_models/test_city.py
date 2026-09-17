import unittest
from models.state import State
from models.city import City


class TestUser(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.state = State()
        cls.city = City()

    @class_method
    def tearDownClass(cls):
        del cls.user

    def test_CityName(self):
        self.city.name = "Ikeja"
        self.assertIsInstance(self.user.email, str)

    def test_userPassword(self):
        self.assertIsInstance(self.user.password, str)

    def test_userLastName(self):
        self.assertIsInstance(self.user.lastname, str)

    def test_userFirstName(self):
        self.assertIsInstance(self.user.firstname, str)


if __name__ == '__main__':
    unittest.main()