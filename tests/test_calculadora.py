import pytest
from Calculadora import add, subtract, multiply, divide, power, factorial


class TestAdd:
    """Tests for add function."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        result = add(3, 5)
        assert result == 8

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        result = add(-3, -5)
        assert result == -8

    def test_add_positive_and_negative(self):
        """Test addition of positive and negative number."""
        result = add(5, -3)
        assert result == 2

    def test_add_zero(self):
        """Test addition with zero."""
        result = add(5, 0)
        assert result == 5

    def test_add_floats(self):
        """Test addition of float numbers."""
        result = add(2.5, 3.5)
        assert result == 6.0


class TestSubtract:
    """Tests for subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        result = subtract(8, 3)
        assert result == 5

    def test_subtract_negative_numbers(self):
        """Test subtraction resulting in negative."""
        result = subtract(3, 8)
        assert result == -5

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        result = subtract(5, 0)
        assert result == 5

    def test_subtract_from_zero(self):
        """Test subtraction from zero."""
        result = subtract(0, 5)
        assert result == -5


class TestMultiply:
    """Tests for multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        result = multiply(4, 5)
        assert result == 20

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = multiply(5, 0)
        assert result == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        result = multiply(-3, -4)
        assert result == 12

    def test_multiply_positive_and_negative(self):
        """Test multiplication of positive and negative number."""
        result = multiply(5, -3)
        assert result == -15


class TestDivide:
    """Tests for divide function."""

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        result = divide(10, 2)
        assert result == 5

    def test_divide_resulting_float(self):
        """Test division resulting in float."""
        result = divide(7, 2)
        assert result == 3.5

    def test_divide_by_one(self):
        """Test division by one."""
        result = divide(5, 1)
        assert result == 5

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        result = divide(-10, 2)
        assert result == -5

    def test_divide_by_zero_raises_error(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(10, 0)


class TestPower:
    """Tests for power function."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        result = power(2, 3)
        assert result == 8

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        result = power(5, 0)
        assert result == 1

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        result = power(2, -2)
        assert result == 0.25

    def test_power_one_exponent(self):
        """Test power with exponent one."""
        result = power(5, 1)
        assert result == 5

    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        result = power(4, 0.5)
        assert result == 2.0


class TestFactorialCalculadora:
    """Tests for factorial function in Calculadora."""

    def test_factorial_zero(self):
        """Test factorial of 0 returns 1."""
        result = factorial(0)
        assert result == 1

    def test_factorial_one(self):
        """Test factorial of 1 returns 1."""
        result = factorial(1)
        assert result == 1

    def test_factorial_five(self):
        """Test factorial of 5 returns 120."""
        result = factorial(5)
        assert result == 120

    def test_factorial_seven(self):
        """Test factorial of 7 returns 5040."""
        result = factorial(7)
        assert result == 5040

    def test_factorial_negative_raises_error(self):
        """Test factorial with negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial(-3)
