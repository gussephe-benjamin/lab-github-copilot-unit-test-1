import pytest
from math_utils import generate_fibonacci, factorial

def test_generate_fibonacci():
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    with pytest.raises(ValueError):
        generate_fibonacci(-1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-3)


## Generate unitary test cases for math_utils.py


