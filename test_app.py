
from app import sum_numbers

def test_sum_positive():
    assert sum_numbers(3, 4) == 7

def test_sum_negative():
    assert sum_numbers(-2, -3) == -5

def test_sum_mixed():
    assert sum_numbers(-5, 5) == 0
