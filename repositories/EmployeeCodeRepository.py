from .SpreadSheetService import SpreadSheetService


class EmployeeCodeRepository:


    def __init__(self, id: str, ec: str):
        self.id = id
        self.ec = ec
        self.sheet_service = SpreadSheetService()


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
        self.sheet_service.update_cell(cell.row, cell.col + 3, self.ec)


    def add_ec_not_existing_user(self):
        value = [self.id, None, None, self.ec]
        self.sheet_service.append_row(value)
