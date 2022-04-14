import sys
import unittest
import datetime

sys.path.append('..')
from services.UtilityService import UtilityService
from constants import *

class TestUtilityService(unittest.TestCase):


    def setUp(self):
        pass

    # 要削除
    def test_get_hour(self):
        hour_list = [
            ['1', '01'],
            ['2', '02'],
            ['11', '11']
            ]
        for hour in hour_list:
            ans = hour[0]
            if len(hour[0]) == 1:
                ans = f"0{hour[0]}"
            self.assertEqual(ans, hour[1])

    def test_is_ten_minutes_before(self):
        test = [
            [datetime.datetime.strptime('2022/01/01/10/50', '%Y/%m/%d/%H/%M'), '11', True],
            [datetime.datetime.strptime('2022/01/01/10/52', '%Y/%m/%d/%H/%M'), '11', True],
            [datetime.datetime.strptime('2022/01/01/10/54', '%Y/%m/%d/%H/%M'), '11', True],
            [datetime.datetime.strptime('2022/01/01/10/56', '%Y/%m/%d/%H/%M'), '11', True],
            [datetime.datetime.strptime('2022/01/01/10/58', '%Y/%m/%d/%H/%M'), '11', True],
            [datetime.datetime.strptime('2022/01/01/11/00', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/11/00', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/11/00', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/23/30', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/23/40', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/10/00', '%Y/%m/%d/%H/%M'), '10', False],
            [datetime.datetime.strptime('2022/01/01/09/50', '%Y/%m/%d/%H/%M'), '10', True],
            [datetime.datetime.strptime('2022/01/01/09/49', '%Y/%m/%d/%H/%M'), '10', False],
            [datetime.datetime.strptime('2022/01/01/09/59', '%Y/%m/%d/%H/%M'), '10', True],
            [datetime.datetime.strptime('2022/01/01/20/15', '%Y/%m/%d/%H/%M'), '20', False],
            [datetime.datetime.strptime('2022/01/01/19/50', '%Y/%m/%d/%H/%M'), '20', True],
        ]
        for case in test:
            us = UtilityService()
            self.assertEqual(us.is_ten_minutes_before(case[0], case[1]), case[2])

    def test_is_ten_minutes_after(self):
        test = [
            [datetime.datetime.strptime('2022/01/01/10/50', '%Y/%m/%d/%H/%M'), '11', False],
            [datetime.datetime.strptime('2022/01/01/10/52', '%Y/%m/%d/%H/%M'), '11', False],
            [datetime.datetime.strptime('2022/01/01/10/54', '%Y/%m/%d/%H/%M'), '11', False],
            [datetime.datetime.strptime('2022/01/01/10/56', '%Y/%m/%d/%H/%M'), '11', False],
            [datetime.datetime.strptime('2022/01/01/10/58', '%Y/%m/%d/%H/%M'), '11', False],
            [datetime.datetime.strptime('2022/01/01/11/00', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/11/00', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/11/00', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/23/30', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/23/40', '%Y/%m/%d/%H/%M'), '00', False],
            [datetime.datetime.strptime('2022/01/01/10/00', '%Y/%m/%d/%H/%M'), '10', False],
            [datetime.datetime.strptime('2022/01/01/09/50', '%Y/%m/%d/%H/%M'), '10', False],
            [datetime.datetime.strptime('2022/01/01/09/49', '%Y/%m/%d/%H/%M'), '10', False],
            [datetime.datetime.strptime('2022/01/01/09/59', '%Y/%m/%d/%H/%M'), '10', False],
            [datetime.datetime.strptime('2022/01/01/20/15', '%Y/%m/%d/%H/%M'), '20', True],
            [datetime.datetime.strptime('2022/01/01/19/50', '%Y/%m/%d/%H/%M'), '20', False],
            [datetime.datetime.strptime('2022/01/01/19/10', '%Y/%m/%d/%H/%M'), '19', True],
        ]
        for case in test:
            us = UtilityService()
            self.assertEqual(us.is_ten_minutes_after(case[0], case[1]), case[2])

    def test_is_valid_time(self):
        test = [
            ['00', True],
            ['01', True],
            ['10', True],
            ['20', True],
            ['24', False],
            [10, False],
            ['000', False]
        ]
        for case in test:
            us = UtilityService()
            self.assertEqual(us.is_valid_time(case[0]), case[1])


    def test_is_first_batch(self):
        test = [
            [datetime.datetime.strptime('2022/01/01/10/50', '%Y/%m/%d/%H/%M'), False],
            [datetime.datetime.strptime('2022/01/01/00/20', '%Y/%m/%d/%H/%M'), False],
            [datetime.datetime.strptime('2022/01/01/00/00', '%Y/%m/%d/%H/%M'), True],
            [datetime.datetime.strptime('2022/01/01/00/09', '%Y/%m/%d/%H/%M'), True],
            [datetime.datetime.strptime('2022/01/01/00/10', '%Y/%m/%d/%H/%M'), False],
            [datetime.datetime.strptime('2022/01/01/23/59', '%Y/%m/%d/%H/%M'), False],
        ]

        for case in test:
            us = UtilityService()
            self.assertEqual(us.is_first_batch(case[0]), case[1])

if __name__ == "__main__":
    unittest.main()
