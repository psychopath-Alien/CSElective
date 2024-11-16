from unittest import mock
import pytest
from functions import UserGuess

def test_generate_numbers():
    with mock.patch('random.randint', return_value = 5):
        assert UserGuess.generate_number() == 5

def test_user_input_validation():
    assert UserGuess.is_user_input_digit("123") == True
    assert UserGuess.is_user_input_digit("abc") == False
    assert UserGuess.is_user_input_digit("abc123!#$%^") == False
    
def test_user_input_range():
    assert UserGuess.is_user_input_in_range("100") == True
    assert UserGuess.is_user_input_in_range("1") == True
    assert UserGuess.is_user_input_in_range("101") == False
    assert UserGuess.is_user_input_in_range("-1") == False

def test_user_guessed_the_number():
    user_input = 42
    rand_input = 42
    assert UserGuess.is_user_guess_the_number(user_input, rand_input) == True

def test_user_not_guessed_the_number():
    user_input = 42
    rand_input = 21
    assert UserGuess.is_user_guess_the_number(user_input, rand_input) == False

def test_user_input_is_greater():
    user_input = 29
    rand_input = 12
    assert UserGuess.is_user_input_is_greater(user_input, rand_input) == True

def test_user_input_is_lesser():
    user_input = 21
    rand_input = 42
    assert UserGuess.is_user_input_is_greater(user_input, rand_input) == False