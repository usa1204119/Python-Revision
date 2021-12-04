import unittest
from city_country import city_country

class CityTestCase(unittest.TestCase):
    """ Testing city_country.py """
    def test_city_country(self):
        """ Will name like Mumbai, India work ? """
        city = city_country('mumbai', 'India')
        self.assertEqual(city,'Mumbai, India')

    def test_city_country_population(self):
        """ Will name like Mumbai, India-19000000 """
        city = city_country('mumbai','india',19000000)
        self.assertEqual(city,'Mumbai, India-19000000')
unittest.main()