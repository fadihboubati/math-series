from math_series import __version__
from math_series.math_series import fibonacci ,lucas,sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_ten():
    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_sum_series_five():
    actual = sum_series(5)
    expected = {'fibonacci_result':5,'luces_result':11}
    assert actual == expected

def test_sum_series_ten():
    actual = sum_series(10)
    expected = {'fibonacci_result':55,'luces_result':123}
    assert actual == expected
