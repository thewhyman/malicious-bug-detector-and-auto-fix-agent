import os
import uuid
import tempfile


def create_temp_file_path() -> str:
    """
    Generate a unique temporary file path without creating the file.

    Returns a unique path string located in the system's temporary directory.
    The file itself is NOT created — only the path is returned.

    Returns:
        str: A unique absolute path in the system temp directory.
    """
    temp_dir = tempfile.gettempdir()
    unique_filename = uuid.uuid4().hex
    temp_file_path = os.path.join(temp_dir, unique_filename)
    return temp_file_path