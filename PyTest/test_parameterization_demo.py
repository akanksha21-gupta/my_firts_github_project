import pytest

def sum(a, b):
    return a + b

def test_sum_1():
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 1