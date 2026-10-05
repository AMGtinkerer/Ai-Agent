import os
from config import MAX_CHARS



def get_file_content(working_directory: str, file_path: str) -> str:

    try:

        abs_working_dir = os.path.abspath(working_directory)
        combined_path = os.path.join(abs_working_dir, file_path)
        normalized_path = os.path.normpath(combined_path)
        valid_target_dir =os.path.commonpath([abs_working_dir, normalized_path]) == abs_working_dir
        is_file = os.path.isfile(normalized_path)

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

    

        with open(normalized_path, "r") as file:
            file_content_string = file.read(MAX_CHARS)
        
            if file.read(1) != "":  # Check if there's more content beyond MAX_CHARS
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string

    except Exception as e:
        return f"Error: {e}"


