import os




def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:

        abs_working_dir = os.path.abspath(working_directory)
        combined_path = os.path.join(abs_working_dir, file_path)
        normalized_path = os.path.normpath(combined_path)
        valid_target_dir = os.path.commonpath([abs_working_dir, normalized_path]) == abs_working_dir

        is_dir = os.path.isdir(normalized_path)

        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'




        os.makedirs(os.path.dirname(normalized_path), exist_ok=True)
        with open(normalized_path, "w") as file:
            file.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a file within the working directory, creating directories as needed.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
        "required": ["file_path", "content"], #must have these to operate
    
                }
            }
        }
    }
