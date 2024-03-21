import pytest

# Basic assertion
def test_basic_assertion():
    assert True  # Asserts that the condition is True

# Assert Equal
def test_assert_equal():
    expected = 5
    actual = 5
    assert expected == actual  # Asserts that expected value equals actual value

# Assert Not Equal
def test_assert_not_equal():
    expected = 5
    actual = 10
    assert expected != actual  # Asserts that expected value does not equal actual value

# Assert In
def test_assert_in():
    container = [1, 2, 3, 4, 5]
    item = 3
    assert item in container  # Asserts that item is present in container

# Assert Not In
def test_assert_not_in():
    container = [1, 2, 3, 4, 5]
    item = 6
    assert item not in container  # Asserts that item is not present in container

# Assert True/False
def test_assert_true_false():
    condition = True
    assert condition is True  # Asserts that condition is True

    condition = False
    assert condition is False  # Asserts that condition is False

# Assert Greater/Equal
def test_assert_greater_equal():
    value = 10
    other_value = 5
    assert value > other_value  # Asserts that value is greater than other_value
    assert value >= other_value  # Asserts that value is greater than or equal to other_value

# Assert Less/Equal
def test_assert_less_equal():
    value = 5
    other_value = 10
    assert value < other_value  # Asserts that value is less than other_value
    assert value <= other_value  # Asserts that value is less than or equal to other_value

# Assert Raises
def test_assert_raises():
    def raise_exception():
        raise ValueError("Error!")

    with pytest.raises(ValueError):  # Asserts that the specified exception is raised
        raise_exception()
