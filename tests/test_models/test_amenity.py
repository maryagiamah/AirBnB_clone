import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.amenity = Amenity()

    @class_method
    def tearDownClass(cls):
        del cls.amenity

    def test_amenityName(self):
        self.amenity.name = "Light"
        self.assertEqual(self.amenity.name, "Light")


if __name__ == '__main__':
    unittest.main()