import unittest
from models.user import User
from models.city import City
from models.amenity import Amenity
from model.place import Place


class TestPlace(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.user = User()
        cls.city = City()
        cls.amenity = Amenity()
        cls.place = Place()

    @class_method
    def tearDownClass(cls):
        del cls.user
        del cls.city
        del cls.amenity
        del cls.place

    def test_placeName(self):
        self.place.name = "National Park"
        self.assertEqual(self.place.name, "National Park")

    def test_placeCity(self):
        self.place.city_id = self.city.id
        self.assertEqual(self.place.city_id, self.city.id)

    def test_placeUser(self):
        self.place.user_id = self.user.id
        self.assertEqual(self.place.user_id, self.user.id)

    def test_placeDescription(self):
        self.place.description = "A place to unwind and relax"
        self.assertEqual(self.place.description, "A place to unwind and relax")

    def test_placeNumbRooms(self):
        self.assertEqual(self.place.number_rooms, 0)

    def test_placeNumbBathrooms(self):
        self.place.number_bathrooms = 12
        self.assertEqual(self.place.number_bathrooms, 12)

    def test_placeMaxGuest(self):
        self.place.max_guest = 15
        self.assertEqual(self.place.max_guest, 15)

    def test_placeNightPrice(self):
        self.assertEqual(self.price_by_night, 0)

    def test_placeLatitude(self):
        self.place.latitude = 6.615213
        self.assertEqual(self.place.latitude, 6.615213)

    def test_placeLongitude(self):
        self.place.longitude = 3.363948
        self.assertEqual(self.place.longitude, 3.363948)

    def test_placeAmenities(self):
        self.place.amenity_ids.append(self.amenity.id)
        self.assertEqual(self.place.amenity_ids, [self.amenity.id])



if __name__ == '__main__':
    unittest.main()
