import pytest

@pytest.fixture(scope="session", autouse=True)
def setUp():
    print("Launch browser")
    print("Login")
    print("browse products")
    yield # After / Tear Down
    print("Logoff")
    print("Close Browser")

