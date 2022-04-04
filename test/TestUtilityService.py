import sys
import unittest

sys.path.append('..')
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


if __name__ == "__main__":
    unittest.main()
