import pytest

@pytest.fixture(params=["a","b"])
def demo_fixture(request):
    print(request.param)

def testLogin(demo_fixture):
    print("Login Successful")


def testLogoff():
    print("Logout Successful")


def testCalculation():
    assert 2 + 2 == 4
