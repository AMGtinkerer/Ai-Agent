import os

#validates the directory and lists the files in it, along with their sizes and whether they are directories or not
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

    
        item_list = os.listdir(target_directory)

        files_info = []

        for item in item_list:
            filepath = os.path.join(target_directory, item)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            
            info_string = f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            files_info.append(info_string)

        files_info_str = "\n".join(files_info)

        return files_info_str
        




    except Exception as e:
        return f"Error: {e}"


    
