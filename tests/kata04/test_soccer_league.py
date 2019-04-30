import unittest

from code_kata.kata04.soccer_league import smallest_difference


class SoccerLeagueTestSuite(unittest.TestCase):
    """Basic test cases for Kata 04 - Data Munging."""

    @unittest.skip("not yet implemented")
    def test_no_data(self):
        self.assertEqual(0, smallest_difference([]))


if __name__ == '__main__':
    unittest.main()
