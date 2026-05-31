import pytest
from app import reverse_string


def test_reverse_simple_string():
    assert reverse_string("hello") == "olleh"


def test_reverse_empty_string():
    assert reverse_string("") == ""


def test_reverse_single_character():
    assert reverse_string("a") == "a"


def test_reverse_palindrome():
    assert reverse_string("racecar") == "racecar"


def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


def test_reverse_string_with_special_characters():
    assert reverse_string("!@#$%") == "%$#@!"


def test_reverse_string_with_numbers():
    assert reverse_string("12345") == "54321"


def test_reverse_mixed_case_string():
    assert reverse_string("HeLLo WoRLd") == "dLRoW oLLeH"


def test_reverse_string_with_unicode():
    assert reverse_string("héllo") == "olléh"


def test_reverse_raises_type_error_for_non_string_int():
    with pytest.raises(TypeError):
        reverse_string(123)


def test_reverse_raises_type_error_for_non_string_list():
    with pytest.raises(TypeError):
        reverse_string(["h", "e", "l", "l", "o"])


def test_reverse_raises_type_error_for_none():
    with pytest.raises(TypeError):
        reverse_string(None)


def test_reverse_raises_type_error_for_dict():
    with pytest.raises(TypeError):
        reverse_string({"key": "value"})


def test_reverse_long_string():
    long_string = "a" * 10000
    assert reverse_string(long_string) == long_string


def test_reverse_newline_characters():
    assert reverse_string("line1\nline2") == "2enil\n1enil"
