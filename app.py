import base64


def encode_to_base64(input_string: str, encoding: str = "utf-8") -> str:
    """
    Encode a string to a base64 representation.

    Args:
        input_string: The string to encode.
        encoding: The character encoding to use (default: 'utf-8').

    Returns:
        A base64-encoded string.

    Raises:
        TypeError: If input_string is not a string.
        ValueError: If the encoding is invalid or unsupported.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected str, got {type(input_string).__name__}")

    try:
        encoded_bytes = input_string.encode(encoding)
    except LookupError as exc:
        raise ValueError(f"Unknown encoding: {encoding}") from exc

    return base64.b64encode(encoded_bytes).decode("ascii")


def decode_from_base64(base64_string: str, encoding: str = "utf-8") -> str:
    """
    Decode a base64-encoded string back to a plain string.

    Args:
        base64_string: The base64-encoded string to decode.
        encoding: The character encoding to use when decoding bytes (default: 'utf-8').

    Returns:
        The decoded plain string.

    Raises:
        TypeError: If base64_string is not a string.
        ValueError: If the input is not valid base64 or the encoding is invalid.
    """
    if not isinstance(base64_string, str):
        raise TypeError(f"Expected str, got {type(base64_string).__name__}")

    try:
        decoded_bytes = base64.b64decode(base64_string, validate=True)
    except Exception as exc:
        raise ValueError(f"Invalid base64 input: {exc}") from exc

    try:
        return decoded_bytes.decode(encoding)
    except LookupError as exc:
        raise ValueError(f"Unknown encoding: {encoding}") from exc
    except UnicodeDecodeError as exc:
        raise ValueError(f"Cannot decode bytes with encoding '{encoding}': {exc}") from exc