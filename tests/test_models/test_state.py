import unittest
from models.state import State


class TestState(unittest.TestCase):

    @class_method
    def setUpClass(cls):
        cls.state = State()

    @class_method
    def tearDownClass(cls):
        del cls.state

    def test_stateName(self):
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()