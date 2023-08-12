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
        with self.assertRaises(TypeError) as err:
            storage.all("exess")
        self.assertEqual(str(err.exception), 'FileStorage.all() takes 1'
                         + ' positional argument but 2 were given')
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_save(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.save("exess")
        self.assertEqual(str(err.exception), 'FileStorage.save() takes 1'
                         + ' positional argument but 2 were given')
        storage.save()
        file_name = storage._FileStorage__file_path
        self.assertTrue(path.exists(file_name))
