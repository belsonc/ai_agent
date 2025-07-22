from functions.get_files_info import get_file_content
from functions.get_files_info import write_file
from functions.run_python import run_python_file


#adding a comment to edit the file so i can keep the streak alive
#print (get_file_content("calculator", "lorem.txt"))
#print (get_file_content("calculator", "main.py"))
#print (get_file_content("calculator", "pkg/calculator.py"))
#print (get_file_content("calculator", "/bin/cat"))

    #remove your old tests from tests.py and add three new ones, as always print the results of each:
#print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))