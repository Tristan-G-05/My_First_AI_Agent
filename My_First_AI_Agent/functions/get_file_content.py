import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

    try:
        # Construct the full path to the file and ensure it's within the working directory
        working_dir_abs = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if the file exists
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read and return the content of the file
        with open(full_path, 'r') as f:
            content = f.read(MAX_CHARS)  # Limit the content to 10,000 characters
            if f.read(1):  # Check if there's more content beyond the limit
                content += f'... File "{file_path}" truncated at {MAX_CHARS} characters.'
        return content
    except Exception as e:
        return f'Error: Could not read file "{file_path}": {e}'