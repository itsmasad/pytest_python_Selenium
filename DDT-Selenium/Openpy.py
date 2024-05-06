import openpyxl.workbook
import pytest
import openpyxl

def read_data():
    workbook = openpyxl.load_workbook("DDT-Selenium\exelsheet\workbook.xlsx")
    sheet = workbook.active
    test_data = []
    for row in sheet.iter_rows(min_row=1,min_col=1,max_row=4,max_col=2,values_only=True):
        username,password = row
        test_data.append((username,password))
    return test_data


@pytest.mark.parametrize("Username,Password",read_data())
def test_Para(Username,Password):
    print(f'{Username} & {Password}')