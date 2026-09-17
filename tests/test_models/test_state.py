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
        self.state.name = "Lagos"
        self.assertEqual(self.state.name, "Lagos")


if __name__ == '__main__':
    unittest.main()