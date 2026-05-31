import pytest
from app import encode_to_base64, decode_from_base64


# ---------------------------------------------------------------------------
# encode_to_base64 tests
# ---------------------------------------------------------------------------

class TestEncodeToBase64:
    def test_simple_ascii_string(self):
        assert encode_to_base64("hello") == "aGVsbG8="

    def test_empty_string(self):
        assert encode_to_base64("") == ""

    def test_single_character(self):
        assert encode_to_base64("A") == "QQ=="

    def test_string_with_spaces(self):
        assert encode_to_base64("hello world") == "aGVsbG8gd29ybGQ="

    def test_string_with_newline(self):
        assert encode_to_base64("line1\nline2") == "bGluZTEKbGluZTI="

    def test_string_with_tab(self):
        assert encode_to_base64("col1\tcol2") == "Y29sMQljb2wy"

    def test_numeric_string(self):
        assert encode_to_base64("1234567890") == "MTIzNDU2Nzg5MA=="

    def test_special_characters(self):
        result = encode_to_base64("!@#$%^&*()")
        assert isinstance(result, str)
        # Round-trip check
        assert decode_from_base64(result) == "!@#$%^&*()"

    def test_unicode_string_utf8(self):
        result = encode_to_base64("héllo")
        assert isinstance(result, str)
        assert decode_from_base64(result) == "héllo"

    def test_unicode_emoji(self):
        result = encode_to_base64("😀🎉")
        assert isinstance(result, str)
        assert decode_from_base64(result) == "😀🎉"

    def test_chinese_characters(self):
        result = encode_to_base64("你好世界")
        assert isinstance(result, str)
        assert decode_from_base64(result) == "你好世界"

    def test_long_string(self):
        long_str = "a" * 10_000
        result = encode_to_base64(long_str)
        assert decode_from_base64(result) == long_str

    def test_returns_ascii_string(self):
        result = encode_to_base64("test")
        result.encode("ascii")  # Should not raise

    def test_non_string_raises_type_error(self):
        with pytest.raises(TypeError):
            encode_to_base64(123)  # type: ignore

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            encode_to_base64(None)  # type: ignore

    def test_list_raises_type_error(self):
        with pytest.raises(TypeError):
            encode_to_base64(["hello"])  # type: ignore

    def test_invalid_encoding_raises_value_error(self):
        with pytest.raises(ValueError, match="Unknown encoding"):
            encode_to_base64("hello", encoding="not-a-real-encoding")

    def test_latin1_encoding(self):
        result = encode_to_base64("café", encoding="latin-1")
        assert isinstance(result, str)
        assert decode_from_base64(result, encoding="latin-1") == "café"

    def test_output_has_no_whitespace(self):
        result = encode_to_base64("some text here")
        assert " " not in result
        assert "\n" not in result


# ---------------------------------------------------------------------------
# decode_from_base64 tests
# ---------------------------------------------------------------------------

class TestDecodeFromBase64:
    def test_simple_ascii_string(self):
        assert decode_from_base64("aGVsbG8=") == "hello"

    def test_empty_string(self):
        assert decode_from_base64("") == ""

    def test_single_character(self):
        assert decode_from_base64("QQ==") == "A"

    def test_string_with_spaces(self):
        assert decode_from_base64("aGVsbG8gd29ybGQ=") == "hello world"

    def test_string_with_newline(self):
        assert decode_from_base64("bGluZTEKbGluZTI=") == "line1\nline2"

    def test_numeric_string(self):
        assert decode_from_base64("MTIzNDU2Nzg5MA==") == "1234567890"

    def test_invalid_base64_raises_value_error(self):
        with pytest.raises(ValueError, match="Invalid base64 input"):
            decode_from_base64("not_valid_base64!!!")

    def test_invalid_base64_wrong_padding_raises_value_error(self):
        with pytest.raises(ValueError):
            decode_from_base64("aGVsbG8")  # missing padding, validate=True strict

    def test_non_string_raises_type_error(self):
        with pytest.raises(TypeError):
            decode_from_base64(12345)  # type: ignore

    def test_none_raises_type_error(self):
        with pytest.raises(TypeError):
            decode_from_base64(None)  # type: ignore

    def test_bytes_raises_type_error(self):
        with pytest.raises(TypeError):
            decode_from_base64(b"aGVsbG8=")  # type: ignore

    def test_invalid_encoding_raises_value_error(self):
        with pytest.raises(ValueError, match="Unknown encoding"):
            decode_from_base64("aGVsbG8=", encoding="not-a-real-encoding")

    def test_latin1_encoding(self):
        import base64
        raw = "café".encode("latin-1")
        b64 = base64.b64encode(raw).decode("ascii")
        assert decode_from_base64(b64, encoding="latin-1") == "café"

    def test_unicode_emoji_round_trip(self):
        encoded = encode_to_base64("🚀✨")
        assert decode_from_base64(encoded) == "🚀✨"

    def test_long_string_round_trip(self):
        original = "The quick brown fox jumps over the lazy dog. " * 500
        assert decode_from_base64(encode_to_base64(original)) == original


# ---------------------------------------------------------------------------
# Round-trip tests
# ---------------------------------------------------------------------------

class TestRoundTrip:
    @pytest.mark.parametrize("text", [
        "",
        "a",
        "hello",
        "Hello, World!",
        "1234567890",
        "!@#$%^&*()-_=+[]{}|;':\",./<>?",
        "line1\nline2\nline3",
        "tab\there",
        "  leading and trailing spaces  ",
        "null\x00byte",
        "café résumé naïve",
        "日本語テスト",
        "🎉🔥💯",
        "mixed: hello 世界 🌍",
    ])
    def test_encode_decode_roundtrip(self, text):
        assert decode_from_base64(encode_to_base64(text)) == text

    def test_multiple_encode_decode_cycles(self):
        original = "hello world"
        result = original
        for _ in range(5):
            result = encode_to_base64(result)
        for _ in range(5):
            result = decode_from_base64(result)
        assert result == original