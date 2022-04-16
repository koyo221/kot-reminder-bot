import sys
import unittest

sys.path.append('..')
from constants import *
from services.KingOfTimeService import KingOfTimeService


class TestKingOfTimeService(unittest.TestCase):

    def setUp(self):
        pass

    def test_stamp(self):
        test = [
            ['U0fe4c65c75dcbffc15ae1b249ed1c8f3', 'NO_EMPLOYEE_KEY_ERROR']
        ]
        for case in test:
            kots = KingOfTimeService()
            self.assertEqual(kots.stamp(case[0]), case[1])

if __name__ == "__main__":
    unittest.main()
