from services.LineService import LineService
from .SpreadSheetService import SpreadSheetService


class EmployeeCodeRepository:


    def __init__(self, id: str, ec: str):
        self.id = id
        self.ec = ec
        self.sheet_service = SpreadSheetService()
        self.line_service = LineService()


    def register_ec(self):
        cell = self.sheet_service.find(self.id)
        if (cell is None):
            self.add_ec_not_existing_user()
        else:
            self.add_ec_existing_user(cell)


    def is_already_registered(self):
        cell  = self.sheet_service.find(self.ec)
        if cell is None:
            return False
        return True


    def add_ec_existing_user(self, cell):
        display_name = self.line_service.get_display_name(self.id)
        # 従業員コードを更新
        self.sheet_service.update_cell(cell.row, cell.col + 3, self.ec)

        # 表示名を更新
        self.sheet_service.update_cell(cell.row, cell.col + 5, display_name)

        # 打刻カウントを更新
        self.sheet_service.update_cell(cell.row, cell.col + 7, 0)


    def add_ec_not_existing_user(self):
        display_name = self.line_service.get_display_name(self.id)
        value = [self.id, None, None, self.ec, None, display_name, None, 0]
        self.sheet_service.append_row(value)
