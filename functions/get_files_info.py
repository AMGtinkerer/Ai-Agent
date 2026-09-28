import os


def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        abs_working_directory = os.path.abspath(working_directory)
     
    
        target_directory = os.path.normpath(os.path.join(abs_working_directory, directory))
   

        valid_target_dir = os.path.commonpath([abs_working_directory, target_directory]) == abs_working_directory

    
    
    


    
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    

    

        is_directory = os.path.isdir(target_directory)


        if not is_directory:
            return f'Error: "{directory}" is not a directory'

    
        if is_directory:
            return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"
