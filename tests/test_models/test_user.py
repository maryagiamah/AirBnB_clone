import unittest
from models.user import User


class TestUser(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.user = User()

    @class_method
    def tearDownClass(cls):
        del cls.user

    def test_userEmail(self):
        self.assertIsInstance(self.user.email, str)

    def test_userPassword(self):
        self.assertIsInstance(self.user.password, str)

    def test_userLastName(self):
        self.assertIsInstance(self.user.lastname, str)

    def test_userFirstName(self):
        self.assertIsInstance(self.user.firstname, str)
