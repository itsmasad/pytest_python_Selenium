import pytest

# Use skip marker to skip a particular test

@pytest.mark.skip
def testLogin():
    print("Login Successful")

# Custom markers
@pytest.mark.regression
def testLogoff():
    print("Logout Successful")

@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4

# expected fail test case marker

# @pytest.mark.xfail
def testfunction():
    assert 1 + 2 == 2
