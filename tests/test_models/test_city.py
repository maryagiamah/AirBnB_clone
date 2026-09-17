import unittest
from models.state import State
from models.city import City


class TestCity(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.state = State()
        cls.city = City()

    @class_method
    def tearDownClass(cls):
        del cls.city
        del cls.state

    def test_CityName(self):
        self.city.name = "Ikeja"
        self.assertEqual(self.city.name, "IKeja")

    def test_cityState(self):
        self.city.state_id = self.state.id
        self.assertEqual(self.city.state_id, self.state.id)


if __name__ == '__main__':
    unittest.main()