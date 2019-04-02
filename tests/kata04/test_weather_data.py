from tests.kata04.context import smallest_spread

import unittest


class WeatherDataTestSuite(unittest.TestCase):
    """Basic test cases for Kata 04 - Data Munging."""

    def test_no_data(self):
        self.assertEqual(0, smallest_spread([]))


if __name__ == '__main__':
    unittest.main()
