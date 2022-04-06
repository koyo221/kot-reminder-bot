import sys
import unittest

sys.path.append('..')
from constants import *
from services.MatcherService import MatcherService


class TestMatcherService(unittest.TestCase):


    def setUp(self):
        pass


    def test_is_valid_worktime(self):
        test_msg = [
            ['11/11', 'invalid'],
            ['11/12', ['11', '12']],
            ['aaaa', False],
            ['aa/aa', False],
            ['12/a1', False],
            ['00/00', 'invalid'],
            ['99/22', 'invalid'],
            ['30/50', 'invalid']
        ]

        for case in test_msg:
            self.matcher_service = MatcherService(case[0])
            res = self.matcher_service.is_valid_worktime()
            self.assertEqual(case[1], res)


    def test_match(self):
        test_msg = [
            ['11/11', 'no_match'],
            ['aaaa', 'no_match'],
            ['aa/aa', 'no_match'],
            ['12/a1', 'no_match'],
            ['00/00', 'no_match'],
            ['退勤', 'REQUEST_LEAVE'],
            ['article', 'REQUEST_ARTICLES'],
            ['ざん', 'REQUEST_OVERWORK']
        ]

        for case in test_msg:
            self.matcher_service = MatcherService(case[0])
            res = self.matcher_service.match(
                RequestConst)
            self.assertEqual(case[1], res)


if __name__ == "__main__":
    unittest.main()
