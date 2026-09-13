import unittest
import os
from models.engine import file_storage


Class Test_FileStorage(unittest.Testcase):
    def setUpClass(cls):
        cls.storage = file_storage.FileStorage()

    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)
    def test_file