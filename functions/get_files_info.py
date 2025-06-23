import os

def get_files_info(working_directory, directory=None):
    if directory != working_directory:
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(directory):
        raise Exception(f'Error: "{directory}" is not a directory')
    