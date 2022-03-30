from repositories.SpreadSheet import SpreadSheet

class WorkTimeRepository(SpreadSheet):


    def __init__(self, user_id, start_time, end_time) -> None:
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time


    # def test(self):
    #     value = [self.user_id, self.start_time, self.end_time]
    #     body = {
    #         "user_id": self.user_id,
    #         "start_time": self.start_time,
    #         "end_time": self.end_time
    #     }
    #     res = super().sheets.sheet1.append_row(value)
    #     return res

    # def find(self):
    #     res = super().sheets.sheet1.find('abcdefghijk1').row
    #     return res

    def find_matching_id(self):
        return super().sheets.sheet1.find(self.user_id)

    def update_worktime(self):
        id = self.find_matching_id()
        try:
            if (id is None):
                value = [self.user_id, self.start_time, self.end_time]
                super().sheets.sheet1.append_row(value)
        except:
            return False

        try:
            super().sheets.sheet1.update_cell(id.row, id.col + 1, self.start_time)
            super().sheets.sheet1.update_cell(id.row, id.col + 2, self.end_time)
        except:
            return False

        return True