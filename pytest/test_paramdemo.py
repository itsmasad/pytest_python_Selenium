import pytest

@pytest.mark.parametrize("username,password",[("asad","1234"),("sajid","5678"),("naveed","0000")])
def test_sampleone(username,password):
    print(username+"-"+password)