import unittest
from g_map import Menu


class MenuTest(unittest.TestCase):
    """docstring for carClassTest"""

    def test_menu_instance(self):
        menu = Menu()
        self.assertIsInstance(menu, Menu, msg='The object should be an instance of the `Menu` class')

    def test_object_type(self):
        nairobi = Menu()
        self.assertTrue((type(nairobi) is Menu), msg='The object should be a type of `Menu`')

    def test_default_city_name(self):
        nairobi = Menu()
        self.assertEqual('Nairobi', nairobi.city,
                         msg='The city should be called `Nairobi` if no name was passed as an argument')

if __name__ == '__main__':
    unittest.main()
