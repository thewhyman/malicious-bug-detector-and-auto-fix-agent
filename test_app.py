import pytest
from app import count_vowels


class TestCountVowels:
    """Test suite for the count_vowels function."""

    def test_basic_lowercase_vowels(self):
        """Test counting lowercase vowels."""
        assert count_vowels('hello') == 2

    def test_basic_uppercase_vowels(self):
        """Test counting uppercase vowels."""
        assert count_vowels('HELLO') == 2

    def test_mixed_case_vowels(self):
        """Test counting mixed case vowels."""
        assert count_vowels('HeLLo WoRLd') == 3

    def test_all_vowels_lowercase(self):
        """Test string with all lowercase vowels."""
        assert count_vowels('aeiou') == 5

    def test_all_vowels_uppercase(self):
        """Test string with all uppercase vowels."""
        assert count_vowels('AEIOU') == 5

    def test_no_vowels(self):
        """Test string with no vowels."""
        assert count_vowels('rhythm') == 0

    def test_empty_string(self):
        """Test empty string returns zero."""
        assert count_vowels('') == 0

    def test_string_with_spaces(self):
        """Test string containing spaces."""
        assert count_vowels('a e i o u') == 5

    def test_string_with_numbers(self):
        """Test string containing numbers."""
        assert count_vowels('abc123') == 1

    def test_string_with_special_characters(self):
        """Test string with special characters."""
        assert count_vowels('h@ll0 w0rld!') == 0

    def test_single_vowel(self):
        """Test single vowel character."""
        assert count_vowels('a') == 1

    def test_single_consonant(self):
        """Test single consonant character."""
        assert count_vowels('b') == 0

    def test_repeated_vowels(self):
        """Test string with repeated vowels."""
        assert count_vowels('aaa') == 3

    def test_long_sentence(self):
        """Test a longer sentence."""
        assert count_vowels('The quick brown fox jumps over the lazy dog') == 11

    def test_only_spaces(self):
        """Test string with only spaces."""
        assert count_vowels('   ') == 0

    def test_type_error_with_integer(self):
        """Test that TypeError is raised for integer input."""
        with pytest.raises(TypeError):
            count_vowels(123)

    def test_type_error_with_none(self):
        """Test that TypeError is raised for None input."""
        with pytest.raises(TypeError):
            count_vowels(None)

    def test_type_error_with_list(self):
        """Test that TypeError is raised for list input."""
        with pytest.raises(TypeError):
            count_vowels(['a', 'e', 'i'])

    def test_type_error_with_dict(self):
        """Test that TypeError is raised for dict input."""
        with pytest.raises(TypeError):
            count_vowels({'key': 'value'})

    def test_newline_character(self):
        """Test string with newline characters."""
        assert count_vowels('hello\nworld') == 3

    def test_tab_character(self):
        """Test string with tab characters."""
        assert count_vowels('hello\tworld') == 3
