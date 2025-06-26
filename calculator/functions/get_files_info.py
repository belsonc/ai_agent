#get_files_info.py 

import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = working_directory
    directory_abs_path = os.path.abspath(directory)
    working_directory_abs_path = os.path.abspath(working_directory)
    if not working_directory_abs_path.startswith(directory_abs_path):
#    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(directory):
        return (f'Error: "{directory}" is not a directory')
    
    #build and return a string representing the contents of the directory.  it should use this format:
    #- filename: file_size=### bytes, is_dir=Boolean
    #functions:
    #os.path.abspath()
    #os.path.join()
    #.startswith()
    #os.path.isdir()
    #os.listdir()
    #os.path.getsize()
    #os.path.isfile()
    #.join()

    string_to_return = ""
    for directory_item in os.listdir(directory):
        try:
            filename = directory_item
            filesize = os.path.getsize(os.path.join(directory,directory_item))
            is_a_directory = os.path.isdir(os.path.join(directory,directory_item))
            result = "- " + filename + ": file_size=" + str(filesize) + " bytes, is_dir=" + str(is_a_directory) + "\n"
            string_to_return += result    
        except Exception as e:
            return("Error: " + str(e))
    return string_to_return

def get_file_content(working_directory,file_path):
    return None