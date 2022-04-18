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

    def is_ten_minutes_before(self, dt: datetime.datetime, sheet_hour: str) -> bool:
        """出勤時刻の10分前かどうか

        Args:
            dt (datetime.datetime): 現在時刻
            sheet_hour (str): Spread Sheetから取得した出勤時刻

        Returns:
            bool: 10分前である
        """
        target_hour = int(sheet_hour) - 1 if int(sheet_hour) - 1 != -1 else 23
        is_fifty = 50 <= dt.minute < 60
        return is_fifty and target_hour == dt.hour

    def is_ten_minutes_after(self, dt: datetime.datetime, sheet_hour: str) -> bool:
        """退勤時刻の10分後かどうか

        Args:
            dt (datetime.datetime): 現在時刻
            sheet_hour (str): Spread Sheetから取得した退勤時刻

        Returns:
            bool: 10分後である
        """
        target_hour = int(sheet_hour)
        is_tenth = 10 <= dt.minute < 20
        return is_tenth and target_hour == dt.hour

    #TODO どう考えてももっとマシな書き方があるので、わかったら直す（バグが起きにくいからいいけどね）
    def is_valid_time(self, time: str) -> bool:
        """妥当な時間かどうか

        Args:
            time (str): 入力時刻

        Returns:
            bool: 妥当である
        """
        valid_time = [
            '00', '01', '02', '03', '04', '05',
            '06', '07', '08', '09', '10', '11',
            '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23',
        ]
        return time in valid_time


    def is_first_batch(self, dt: datetime.datetime) ->bool:
        """バッチの初回実行かどうか

        Args:
            dt (datetime.datetime): 時刻

        Returns:
            bool: 初回である
        """
        return (dt.hour == 0) and (00 <= dt.minute < 10)


    def get_date(self):
        return datetime.datetime.now(pytz.timezone('Asia/Tokyo'))


    def get_kot_date(self, dt: datetime.datetime):
        return dt.strftime('%Y-%m-%d')


    def get_kot_time(self, dt: datetime.datetime):
        return f'{dt.isoformat()}'
