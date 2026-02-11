import unittest
from city_functions_2 import city_country


class CityTestCase(unittest.TestCase):
    """test cases for city_functions"""

    def test_cities(self):
        """testing correct output when given two string values"""
        cities = city_country("santiago", "chile")
        self.assertEqual(cities, "Santiago, Chile")

    def test_cities_country_population(self):
        """testing correct output when given two string values"""
        cities = city_country("santiago", "chile", "500000")
        self.assertEqual(cities, "Santiago, Chile - population 500000")


unittest.main()
