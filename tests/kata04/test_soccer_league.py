from tests.kata04.context import smallest_difference

import unittest


class WeatherDataTestSuite(unittest.TestCase):
    """Basic test cases for Kata 04 - Data Munging."""

    def test_no_data(self):
        self.assertEqual(0, smallest_difference([]))


if __name__ == '__main__':
    unittest.main()
