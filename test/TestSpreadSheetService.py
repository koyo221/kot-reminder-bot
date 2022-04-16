import sys
import unittest

sys.path.append('..')
from constants import *
from repositories.SpreadSheetService import SpreadSheetService


class TestSpreadSheetService(unittest.TestCase):

    def setUp(self):
        pass


    def test_get_ek_from_user_id(self):
        test =[
            ['U0fe4c65c75dcbffc15ae1b249ed1c8f3', 'ek']
        ]

        for case in test:
            sss = SpreadSheetService()
            self.assertEqual(sss.get_ek_from_user_id(case[0]) is None, True)


if __name__ == "__main__":
    unittest.main()
