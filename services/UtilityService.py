import random
import datetime, pytz

class UtilityService:


    def slot_true_chance(self, p: float) -> bool:
        """確率pでtrueを返す

        Args:
            p (float): 確率

        Returns:
            bool: 判定の成否
        """
        rng = random.random()
        return p > rng


    def is_weekday(self) -> bool:
        """平日かどうか

        Returns:
            bool: 平日である
        """
        dt = self.get_date()
        return dt.weekday() not in [5, 6]


    def get_hour(self) -> str:
        dt = self.get_date()
        return str(dt.hour)

    def get_date(self):
        return datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
