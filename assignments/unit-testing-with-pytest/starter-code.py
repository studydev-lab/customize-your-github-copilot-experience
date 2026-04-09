import pytest


def add(a: int, b: int) -> int:
    return a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def reverse_string(s: str) -> str:
    return s[::-1]


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Task 1: Basic Unit Tests
def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_mixed():
    assert add(5, -3) == 2


def test_is_prime_true():
    assert is_prime(7) is True


def test_is_prime_false():
    assert is_prime(4) is False


def test_is_prime_edge():
    assert is_prime(1) is False


def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_single():
    assert reverse_string("a") == "a"


# Task 2: Fixtures and Parametrization
@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 5, 7, 11, 13]


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (10, False),
    (17, True),
])
def test_is_prime_parametrized(n, expected):
    assert is_prime(n) == expected


def test_with_fixture(sample_numbers):
    primes = [n for n in sample_numbers if is_prime(n)]
    assert len(primes) == 7


# Task 3: Error Handling and Edge Cases
def test_divide_normal():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_divide_negative():
    assert divide(-10, 2) == -5.0


def test_reverse_string_special():
    assert reverse_string("!@#$") == "$#@!"


def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000
