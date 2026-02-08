import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    
    try:
        # Construct the full path to the file and ensure it's within the working directory
        working_dir_abs = os.path.abspath(working_directory)
        full_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([working_dir_abs, full_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if the file exists and is a Python file
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not full_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        # Construct the command to run the Python file with optional arguments
        command = ['python', full_path]
        if args:
            command.extend(args)

        # Run the command and capture the output
        lines = []
        completed_process = subprocess.run(command, cwd=working_dir_abs, capture_output=True, timeout=30, text=True)
        lines = []

        if completed_process.returncode != 0:
            lines.append(f'Process exited with code {completed_process.returncode}')

        if not completed_process.stdout and not completed_process.stderr:
            lines.append('No output produced')

        if completed_process.stdout:
            lines.append(f'STDOUT:\n{completed_process.stdout}')

        if completed_process.stderr:
            lines.append(f'STDERR:\n{completed_process.stderr}')

        return '\n'.join(lines)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"