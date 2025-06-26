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
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        file_path_abspath = os.path.abspath(os.path.join(working_directory,file_path))
        
    #if the file_path is outside the working directory, return a string with an error
        if not file_path_abspath.startswith(working_directory_abspath):
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    #if the file_path is not a file, again, return an error string
        if not os.path.isfile(file_path):
            return (f'Error: File not found or is not a regular file: "{file_path}"')

    #read the file and return its contents as a string
        MAX_CHARS = 10000
        with open(file_path, "r") as f:
            file_contents = f.read(MAX_CHARS)
            if os.path.getsize(file_path) > MAX_CHARS and len(file_contents) == MAX_CHARS:
                file_contents += f'[...File "{file_path}" truncated at 10000 characters]'

    except Exception as e:
        return ("Error: " + str(e))
    

    #the lesson gives standard library functions to use
    #truncate at 10k characters and append the message to the end

    #update tests.py - remove calls to get_files_info, change it to get_file_content("calculator, "lorem.txt")
    #test that truncating works

    #change lorem.txt to main.py, pkg/calculator.py, and /bin/cat (this one should give an error message)

    return file_contents
#editing to make sure something gets committed
