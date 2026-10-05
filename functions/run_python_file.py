import os
import subprocess



def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:


    try:


        abs_working_dir = os.path.abspath(working_directory)
        combined_path = os.path.join(abs_working_dir, file_path)
        normalized_path = os.path.normpath(combined_path)
        valid_target_dir = os.path.commonpath([abs_working_dir, normalized_path]) == abs_working_dir
        is_file = os.path.isfile(normalized_path)

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        endswith_py = normalized_path.endswith(".py")

        if not endswith_py:
            return f'Error: "{file_path}" is not a Python file'

        
        command = ["python", normalized_path]
        command.extend(args or [])

        result = subprocess.run(command, cwd=abs_working_dir, capture_output=True, text=True, timeout=30)

        output = ""

        if result.returncode != 0:

            output += f"Process exited with code {result.returncode}\n"

        if result.stdout == "" and result.stderr == "":
            output += "No output produced\n"

        
        if result.stdout:
            output += f"STDOUT: {result.stdout}\n"
        if result.stderr:
            output += f"STDERR: {result.stderr}\n"
            
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"

