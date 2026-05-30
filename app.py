def count_vowels(s: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a given string.
    
    Args:
        s: The input string to count vowels in.
        
    Returns:
        The number of vowels found in the string.
        
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise TypeError(f"Expected a string, got {type(s).__name__}")
    
    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)
