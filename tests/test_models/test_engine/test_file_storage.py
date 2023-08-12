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

    def test_new(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.new()
        self.assertEqual(str(err.exception), 'FileStorage.new() missing 1'
                         + " required positional argument: 'obj'")
        with self.assertRaises(TypeError) as err:
            storage.new("obj", "exess")
        self.assertEqual(str(err.exception), 'FileStorage.new() takes 2'
                         + ' positional arguments but 3 were given')

    def test_save(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.save("exess")
        self.assertEqual(str(err.exception), 'FileStorage.save() takes 1'
                         + ' positional argument but 2 were given')
        storage.save()
        file_name = storage._FileStorage__file_path
        self.assertTrue(path.exists(file_name))

    def test_reload(self):
        storage = FileStorage()
        with self.assertRaises(TypeError) as err:
            storage.reload("exess")
        self.assertEqual(str(err.exception), 'FileStorage.reload() takes 1'
                         + ' positional argument but 2 were given')
