import pytest


# Custom Marker
@pytest.mark.regression
def test_regression():
    print("Test 1")


# In build marker


# Telling pytest that we are expecting failier by the marker
@pytest.mark.xfail
def test_regression2():
    print("Test 2")
    assert 3 == 4

