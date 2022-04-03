from .SpreadSheetService import SpreadSheetService

class WorkTimeRepository:


    def __init__(self, id: str, work_time: list[str]):
        self.sheets_service = SpreadSheetService()
        self.id = id
        self.work_time = work_time


    def update_worktime(self):
        cell = self.sheets_service.find(self.id)
        if (cell is None):
            value = [self.id, self.work_time[0], self.work_time[1]]
            self.sheets_service.sheets.sheet1.append_row(value)
        #TODO APIの実行を1回にする
        else:
            self.sheets_service.sheets.sheet1.update_cell(cell.row, cell.col + 1, self.work_time[0])
            self.sheets_service.sheets.sheet1.update_cell(cell.row, cell.col + 2, self.work_time[1])
