import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        file_breakdown = []

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    
        for item in os.listdir(target_dir):
        
            try: 
                item_path = os.path.join(target_dir, item)
                item_size = os.path.getsize(item_path)
                item_is_dir = os.path.isdir(item_path)
                line = f"- {item}: file_size={item_size} bytes, is_dir={item_is_dir}"
            except Exception as e:
                line = f"Error: {item}: Unable to retrieve info: {str(e)}"
            file_breakdown.append(line)
        return "\n".join(file_breakdown)
    except Exception as e:
        return f"Error: Unable to list directory '{directory}': {str(e)}"