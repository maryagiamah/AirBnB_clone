import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base Model"""
    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_save(self):
        self.model.name = "My First Model"
        self.model.id = 89
        self.model.save()

    def test_toDict(self):
        self.model.to_dict()

    def test_id(self):
        self.assertEqual(self.model.id, 89)


if __name__ == '__main__':
    unittest.main()