import pytest

from Calculadora import multiply


def test_multiply_two_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero_right_side():
    assert multiply(7, 0) == 0


def test_multiply_by_zero_left_side():
    assert multiply(0, 9) == 0


def test_multiply_negative_and_positive():
    assert multiply(-5, 6) == -30


def test_multiply_two_negatives():
    assert multiply(-8, -2) == 16


def test_multiply_floats():
    assert multiply(2.5, 4.0) == 10.0


def test_multiply_float_and_integer():
    assert multiply(1.5, 3) == 4.5


def test_multiply_large_numbers():
    assert multiply(1_000_000, 3_000) == 3_000_000_000


def test_multiply_is_commutative():
    a, b = -7, 11
    assert multiply(a, b) == multiply(b, a)


def test_multiply_identity_element_one():
    assert multiply(42, 1) == 42


def test_multiply_float_precision_with_approx():
    assert multiply(0.1, 0.2) == pytest.approx(0.02)
