import openpyxl
import pytest

@pytest.fixture(scope="function")
def test_from_exel():
    print("Open")
    yield
    print("Close")

def openfiledata():
    

@pytest.mark.parametrize("username,password",[("Asad@gmail.com","Password")])
def test_DDT(test_from_exel,username,password):
    print(username,password,) 