import os
import tempfile
import pytest

from app import create_temp_file_path


class TestCreateTempFilePath:
    """Unit tests for the create_temp_file_path() utility function."""

    def test_returns_string(self):
        """The function should return a string."""
        result = create_temp_file_path()
        assert isinstance(result, str)

    def test_path_is_in_temp_directory(self):
        """The returned path should reside inside the system temp directory."""
        result = create_temp_file_path()
        temp_dir = tempfile.gettempdir()
        # Normalise both paths to handle any symlinks or case differences
        assert os.path.normcase(os.path.normpath(result)).startswith(
            os.path.normcase(os.path.normpath(temp_dir))
        )

    def test_file_does_not_exist(self):
        """The function must NOT create the file — only generate the path."""
        result = create_temp_file_path()
        assert not os.path.exists(result), (
            f"create_temp_file_path() must not create the file, but '{result}' exists."
        )

    def test_returns_absolute_path(self):
        """The returned path should be absolute."""
        result = create_temp_file_path()
        assert os.path.isabs(result), f"Expected an absolute path, got: {result}"

    def test_unique_paths(self):
        """Each call should return a different path."""
        paths = {create_temp_file_path() for _ in range(100)}
        assert len(paths) == 100, "Expected 100 unique paths from 100 calls."

    def test_path_parent_is_temp_dir(self):
        """The direct parent directory of the returned path should be the temp dir."""
        result = create_temp_file_path()
        temp_dir = tempfile.gettempdir()
        assert os.path.normcase(os.path.normpath(os.path.dirname(result))) == (
            os.path.normcase(os.path.normpath(temp_dir))
        )

    def test_path_is_non_empty(self):
        """The returned path must not be an empty string."""
        result = create_temp_file_path()
        assert result.strip() != ""

    def test_file_can_be_created_at_path(self):
        """A file can actually be created at the returned path (sanity check)."""
        result = create_temp_file_path()
        try:
            with open(result, "w") as f:
                f.write("test")
            assert os.path.exists(result)
        finally:
            if os.path.exists(result):
                os.remove(result)

    def test_no_side_effects_on_temp_dir(self):
        """Calling the function multiple times should not alter the temp directory."""
        temp_dir = tempfile.gettempdir()
        before = set(os.listdir(temp_dir))
        paths = [create_temp_file_path() for _ in range(10)]
        after = set(os.listdir(temp_dir))
        # None of the newly generated filenames should appear in the directory
        new_entries = after - before
        generated_names = {os.path.basename(p) for p in paths}
        assert generated_names.isdisjoint(new_entries), (
            "create_temp_file_path() must not create any files in the temp directory."
        )