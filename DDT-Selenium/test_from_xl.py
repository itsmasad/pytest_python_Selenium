import openpyxl
import pytest

@pytest.fixture(scope="function")
def test_from_exel():
    print("Open")
    yield
    print("Close")

def openfiledata():
    workbook = openpyxl.load_workbook("DDT-Selenium\\exelsheet\\logindetails.xlsx")
    sheet = workbook.active
    # Initialize lists to store usernames and passwords
    usernames = []
    passwords = []
    # Iterate through rows starting from the 2nd row
    for row in sheet.iter_rows(min_row=2, min_col=1, max_col=2, values_only=True):
        # Read username and password from the row
        username, password = row
        # Append username and password to respective lists
        usernames.append(username)
        passwords.append(password)
    return zip(usernames, passwords)

@pytest.mark.parametrize("username,password", openfiledata())
def test_DDT(test_from_exel, username, password):
    print(username, password)