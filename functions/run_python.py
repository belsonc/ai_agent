#run_python.py
import os

def run_python_file(working_directory, file_path, args=[]):
    

    #if the file_path is outside of the working directory, return a string with an error:
    #f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        file_path_abspath = os.path.abspath(os.path.join(working_directory, file_path))

        if not file_path_abspath.startswith(working_directory_abspath):
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    #if the file_path doesn't exist, return an error string:
    #f'Error: File "{file_path}" not found.'
        if not os.path.exists(file_path_abspath):
            return (f'Error: "{file_path}" not found.')

    #if the file doesn't end in .py, return an error string:
    #f'Error: "{file_path}" is not a Python file.'
        if not file_path_abspath.endswith('.py'):
            return (f'Error: "{file_path}" is not a Python file.')
    #use subprocess.run function to execute the python file
    #-set a timeout of 30 seconds to prevent infinite execution
    #-capture both stdout and stderr
    #-set the working directory properly

    #format the output to include:
    #-the stdout (prefixed with "STDOUT:")
    #-the stderr (prefixed with "STDERR:")
    #-if the process exits with a non-zero code, include "Process exited with code X"
    #-if no out put is produced, return "No output produced."

    #if any exceptions occur during execution, catch them and return an error string:
    #f"Error: executing Python file: {e}"

    #update your tests.py file with these test cases, printing each result:
    #print(run_python_file("calculator", "main.py"))
    #print(run_python_file("calculator", "tests.py"))
    #print(run_python_file("calculator", "../main.py"))
    #print(run_python_file("calculator", "nonexistent.py"))
#july 11 - comment to extend streak
    return None