import pytest

# Use skip marker to skip a particular test

@pytest.fixture()
def setUp():
    print("Launch browser")
    print("Login")
    print("browse products")
    yield # After / Tear Down
    print("Logoff")
    print("Close Browser")


def testAddItemtoCart(setUp):
    print("Add Item Successfully")


def testRemoveItemfromCart(setUp):
    print("Removed Item Successfully")