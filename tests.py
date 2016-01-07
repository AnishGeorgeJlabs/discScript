import unittest

from functions import has_clubbing


class TestClubbing(unittest.TestCase):
    def test_trivial_no_club(self):
        self.assertFalse(has_clubbing("Use this pair of ".lower()))

    def test_with_check_no_club(self):
        self.assertFalse(has_clubbing("With this slack ".lower()))

    def test_club_check(self):
        self.assertTrue(has_clubbing("You can pair it with ".lower()))

    def test_club_check_2(self):
        self.assertFalse(has_clubbing("You can club these ".lower()))


if __name__ == '__main__':
    unittest.main()
