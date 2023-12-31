import unittest
from models.city import City
"""Module for the City class tests"""


class TestCity(unittest.TestCase):
    """Main class for testing City"""

    def test_init(self):
        """
        Tests the attributes of a City instance as well as __init__()
        """
        with self.assertRaises(TypeError) as err:
            City.__init__()

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
