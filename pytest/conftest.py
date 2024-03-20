# In Pytest, the conftest.py file is used to define fixtures, hooks,
# and other configurations that can be shared across multiple test files
# within a directory or package. It serves as a central location for storing common
# fixtures and configuration settings used by tests.



import pytest

@pytest.fixture(scope="session", autouse=True)
def setUp():
    print("Launch browser")
    print("Login")
    print("browse products")
    yield # After / Tear Down
    print("Logoff")
    print("Close Browser")
