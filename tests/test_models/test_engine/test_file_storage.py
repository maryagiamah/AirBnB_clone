import unittest
import os
from models.engine import file_storage
from models.base_model import BaseModel


Class Test_FileStorage(unittest.Testcase):

    @classmethod
    def setUpClass(cls):
        cls.storage = file_storage.FileStorage()
        cls.file_path = cls.storage._FileStorage__file_path
        cls.objects = cls.storage._FileStorage__objects
        cls.model = BaseModel()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
        del cls.model

    def test_filePath(self):
        self.assertIsNotNone(self.file_path)
        self.assertIsInstance(self.file_path, str)

    def test_objects(self):
        self.assertIsInstance(self.objects, dict)

    def test_all(self):
        self assertIs(self.objects, self.storage.all())

    def test_new(self):
        self.storage.new(self.model)
        obj_key = f"BaseModel.{self.model.id}"
        self.assertIn(obj_key, self.objects.keys())

    def test_save(self):
       self.storage.save()
       self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
       self.storage.reload() 