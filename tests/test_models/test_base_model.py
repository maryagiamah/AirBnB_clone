import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base Model"""
    def setUpClass(self):
        self.model = BaseModel()

    def tearDownClass(self):
        del self.model

    def test_save(self):
        self.model.name = "My First Model"
        self.model.id = 89
        self.model.save()

    def test_toDict(self):
        model_json = self.model.to_dict()
        self.assertIsInstance(model_json, dict)

    def test_id(self):
        self.assertEqual(self.model.id, 89)

    def test_create(self):
        self.assertIsNotNone(self.model.created_at)

    def test_print(self):
        str_format = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self assertIsEqual(print(self.model), str_format)
        

if __name__ == '__main__':
    unittest.main()