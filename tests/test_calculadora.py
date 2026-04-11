import pytest

from Calculadora import add, subtract, multiply, divide, power, factorial


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


# --- add ---

def test_add_two_positive_integers():
    assert add(2, 3) == 5

def test_add_positive_and_negative():
    assert add(10, -4) == 6

def test_add_two_negatives():
    assert add(-3, -7) == -10

def test_add_with_zero():
    assert add(5, 0) == 5

def test_add_floats():
    assert add(1.1, 2.2) == pytest.approx(3.3)


# --- subtract ---

def test_subtract_two_positive_integers():
    assert subtract(10, 4) == 6

def test_subtract_result_negative():
    assert subtract(3, 8) == -5

def test_subtract_two_negatives():
    assert subtract(-5, -3) == -2

def test_subtract_with_zero():
    assert subtract(7, 0) == 7

def test_subtract_floats():
    assert subtract(5.5, 2.2) == pytest.approx(3.3)


# --- divide ---

def test_divide_two_positive_integers():
    assert divide(10, 2) == 5.0

def test_divide_result_float():
    assert divide(7, 2) == pytest.approx(3.5)

def test_divide_negative_numerator():
    assert divide(-9, 3) == -3.0

def test_divide_two_negatives():
    assert divide(-8, -4) == 2.0

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


# --- power ---

def test_power_positive_exponent():
    assert power(2, 10) == 1024

def test_power_exponent_zero():
    assert power(5, 0) == 1

def test_power_base_zero():
    assert power(0, 5) == 0

def test_power_negative_exponent():
    assert power(2, -1) == pytest.approx(0.5)

def test_power_float_base():
    assert power(2.0, 3) == pytest.approx(8.0)


# --- factorial ---

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive_integer():
    assert factorial(5) == 120

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_negative_raises():
    with pytest.raises(ValueError, match="not defined for negative"):
        factorial(-1)
