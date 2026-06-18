import pytest
from app import merge_sorted_lists


class TestMergeSortedLists:

    # --- Basic functionality ---

    def test_merge_two_non_overlapping_lists(self):
        assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_two_sorted_lists_with_overlap(self):
        assert merge_sorted_lists([1, 3, 5], [3, 5, 7]) == [1, 3, 3, 5, 5, 7]

    def test_merge_identical_lists(self):
        assert merge_sorted_lists([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]

    def test_merge_lists_of_different_lengths(self):
        assert merge_sorted_lists([1, 2], [3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_lists_where_all_first_list_elements_are_smaller(self):
        assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_merge_lists_where_all_second_list_elements_are_smaller(self):
        assert merge_sorted_lists([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]

    # --- Edge cases with empty lists ---

    def test_merge_empty_list_with_non_empty_list(self):
        assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]

    def test_merge_non_empty_list_with_empty_list(self):
        assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]

    def test_merge_two_empty_lists(self):
        assert merge_sorted_lists([], []) == []

    # --- Single-element lists ---

    def test_merge_single_element_lists(self):
        assert merge_sorted_lists([1], [2]) == [1, 2]

    def test_merge_single_element_lists_reversed(self):
        assert merge_sorted_lists([2], [1]) == [1, 2]

    def test_merge_single_element_lists_equal(self):
        assert merge_sorted_lists([5], [5]) == [5, 5]

    def test_merge_single_element_with_multiple_elements(self):
        assert merge_sorted_lists([3], [1, 2, 4, 5]) == [1, 2, 3, 4, 5]

    # --- Negative numbers ---

    def test_merge_lists_with_negative_numbers(self):
        assert merge_sorted_lists([-5, -3, -1], [-4, -2, 0]) == [-5, -4, -3, -2, -1, 0]

    def test_merge_lists_with_mixed_positive_and_negative(self):
        assert merge_sorted_lists([-3, 0, 3], [-1, 1, 5]) == [-3, -1, 0, 1, 3, 5]

    def test_merge_lists_with_all_negative_numbers(self):
        assert merge_sorted_lists([-10, -5], [-8, -3]) == [-10, -8, -5, -3]

    # --- Duplicate values ---

    def test_merge_lists_with_duplicates_within_same_list(self):
        assert merge_sorted_lists([1, 1, 2], [1, 3, 3]) == [1, 1, 1, 2, 3, 3]

    def test_merge_lists_with_all_same_values(self):
        assert merge_sorted_lists([2, 2, 2], [2, 2]) == [2, 2, 2, 2, 2]

    # --- Float values ---

    def test_merge_lists_with_floats(self):
        assert merge_sorted_lists([1.1, 2.2, 3.3], [1.5, 2.5]) == [1.1, 1.5, 2.2, 2.5, 3.3]

    def test_merge_lists_with_mixed_int_and_float(self):
        result = merge_sorted_lists([1, 3, 5], [2.0, 4.0])
        assert result == [1, 2.0, 3, 4.0, 5]

    # --- Large lists ---

    def test_merge_large_sorted_lists(self):
        list1 = list(range(0, 1000, 2))   # [0, 2, 4, ..., 998]
        list2 = list(range(1, 1001, 2))   # [1, 3, 5, ..., 999]
        expected = list(range(1000))
        assert merge_sorted_lists(list1, list2) == expected

    # --- Result is always sorted ---

    def test_result_is_sorted(self):
        import random
        random.seed(42)
        list1 = sorted(random.sample(range(100), 20))
        list2 = sorted(random.sample(range(100), 20))
        result = merge_sorted_lists(list1, list2)
        assert result == sorted(result)

    def test_result_contains_all_elements(self):
        list1 = [1, 3, 5, 7]
        list2 = [2, 4, 6, 8]
        result = merge_sorted_lists(list1, list2)
        assert sorted(result) == sorted(list1 + list2)

    # --- Type errors ---

    def test_raises_type_error_when_first_arg_is_not_list(self):
        with pytest.raises(TypeError):
            merge_sorted_lists((1, 2, 3), [4, 5, 6])

    def test_raises_type_error_when_second_arg_is_not_list(self):
        with pytest.raises(TypeError):
            merge_sorted_lists([1, 2, 3], "456")

    def test_raises_type_error_when_list_contains_string_elements(self):
        with pytest.raises(TypeError):
            merge_sorted_lists([1, 2, "three"], [4, 5])

    def test_raises_type_error_when_second_list_contains_string_elements(self):
        with pytest.raises(TypeError):
            merge_sorted_lists([1, 2], ["three", "four"])

    def test_raises_type_error_when_list_contains_none(self):
        with pytest.raises(TypeError):
            merge_sorted_lists([1, None, 3], [2, 4])