import os
from config import MAX_CHARS

def write_file(working_directory, file_path, content):

    try:
        # Construct the full path to the file and ensure it's within the working directory
        working_dir_abs = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if the path is a directory
        if os.path.isdir(full_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure the directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Write the content to the file
        with open(full_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: Could not write to file "{file_path}": {e}'