import unittest
from os import path
from models.engine.file_storage import FileStorage
"""Module for the FileStorage class tests"""


class TestFileStorage(unittest.TestCase):
    """Main class for testing FileStorage"""

    def test_init(self):
        """
        Tests the attributes of a FileStorage instance as well as __init__()
        """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, 'creatd_instances.json')
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_save(self):
        storage = FileStorage()
        storage.save()
        file_name = storage._FileStorage__file_path
        self.assertTrue(path.exists(file_name))
