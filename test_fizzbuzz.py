import pytest
from fizzbuzz import fizzbuzz


def test_fizzbuzz_integer():
    with pytest.raises(TypeError):
        fizzbuzz(7.0)


def test_fizzbuzz_positive():
    with pytest.raises(ValueError):
        fizzbuzz(-1)
    with pytest.raises(ValueError):
        fizzbuzz(0)


def test_fizzbuzz_fizz():
    assert fizzbuzz(6) == "Fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(10) == "Buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizzbuzz_other():
    assert fizzbuzz(7) == "Buzz"


