import unittest

from code_kata.kata04.weather_data import smallest_spread


class WeatherDataTestSuite(unittest.TestCase):
    """Basic test cases for Kata 04 - Data Munging."""

    @unittest.skip("not yet implemented")
    def test_no_data(self):
        self.assertEqual(0, smallest_spread([]))


if __name__ == '__main__':
    unittest.main()
