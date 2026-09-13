import unittest
import os
from models.engine import file_storage


Class Test_FileStorage(unittest.Testcase):
    def setUpClass(cls):
        cls.storage = file_storage.FileStorage()
        cls.file_path = cls.storage._FileStorage__file_path
        cls.objects = cls.storage._FileStorage__objects

    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def test_filePath(self):
        self.assertIsNotNone(cls.file_path)
        self.assertIsInstance(cls.file_path, string)

    def test_objects(self):
        self.assertIsInstance(cls.objects, dict)

    def test_all(self):
        self assertIs(cls.objects, cls.storage.all())
        self.assertEqual(cls.objects, {})

    def test_new(self):
        self.model = BaseModel()
        cls.storage.new(self.model)
        obj_key = f"BaseModel.{self.model.id}"
        self.assertIn(obj_key, cls.objects.keys())

    def test_save(self):
       self.model = BaseModel()
       cls.storage.save()
       self.assertTrue(os.path.exists(cls.file_path))

    def test_reload(self):
       cls.storage.reload() 