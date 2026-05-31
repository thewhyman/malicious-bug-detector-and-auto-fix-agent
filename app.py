def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merge two pre-sorted lists of integers into a single sorted list.

    Args:
        list1: A pre-sorted list of integers.
        list2: A pre-sorted list of integers.

    Returns:
        A single sorted list containing all elements from both input lists.

    Raises:
        TypeError: If either input is not a list or contains non-integer elements.
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")

    for item in list1:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be integers or floats, got {type(item)} in list1.")

    for item in list2:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be integers or floats, got {type(item)} in list2.")

    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from list1
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Append any remaining elements from list2
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged