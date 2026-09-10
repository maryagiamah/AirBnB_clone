import unittest
from models.engine import file_storage


Class Test_FileStorage(unittest.Testcase):
    def setUpClass(cls):
        storage = file_storage.FileStorage()
        storage.reload()

    def tearDownClass(cls):
        del self.model