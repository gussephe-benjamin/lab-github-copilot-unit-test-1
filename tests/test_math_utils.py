import pytest
from math_utils import generate_fibonacci, factorial


class TestGenerateFibonacci:
    """Tests for generate_fibonacci function."""

    def test_fibonacci_zero(self):
        """Test fibonacci with n=0 returns empty list."""
        result = generate_fibonacci(0)
        assert result == []

    def test_fibonacci_one(self):
        """Test fibonacci with n=1 returns [0]."""
        result = generate_fibonacci(1)
        assert result == [0]

    def test_fibonacci_two(self):
        """Test fibonacci with n=2 returns [0, 1]."""
        result = generate_fibonacci(2)
        assert result == [0, 1]

    def test_fibonacci_five(self):
        """Test fibonacci with n=5 returns correct sequence."""
        result = generate_fibonacci(5)
        assert result == [0, 1, 1, 2, 3]

    def test_fibonacci_ten(self):
        """Test fibonacci with n=10 returns correct sequence."""
        result = generate_fibonacci(10)
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_negative_raises_error(self):
        """Test fibonacci with negative number raises ValueError."""
        with pytest.raises(ValueError, match="Input must be a non-negative integer."):
            generate_fibonacci(-1)


class TestFactorial:
    """Tests for factorial function."""

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

    def test_factorial_ten(self):
        """Test factorial of 10 returns correct value."""
        result = factorial(10)
        assert result == 3628800

    def test_factorial_negative_raises_error(self):
        """Test factorial with negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial(-5)

    def test_factorial_large_number(self):
        """Test factorial with larger number."""
        result = factorial(7)
        assert result == 5040
