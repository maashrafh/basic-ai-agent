# tests.py

# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
     ### get_files_info tests
     # result = get_files_info("calculator", ".")
     # print(f"Result for current directory:\n{result}")

     # result = get_files_info("calculator", "pkg")
     # print(f"Result for 'pkg' directory:\n{result}")

     # result = get_files_info("calculator", "/bin")
     # print(f"Result for '/bin' directory:\n{result}")

     # result = get_files_info("calculator", "../")
     # print(f"Result for '../' directory:\n{result}")

     ### get_files_content tests
     # result = get_file_content("calculator", "main.py")
     # print(f"Result for lorem.txt: \n{result}")

     # result = get_file_content("calculator", "pkg/calculator.py")
     # print(f"Result for lorem.txt: \n{result}")

     # result = get_file_content("calculator", "/bin/cat")
     # print(f"Result for lorem.txt: \n{result}")

     # result = get_file_content("calculator", "pkg/does_not_exist.py")
     # print(f"Result for lorem.txt: \n{result}")

     ### write_file tests
     # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
     # print(f"Result for writing to lorem.txt: \n{result}")

     # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
     # print(f"Result for writing to pkg/morelorem.txt: \n{result}")

     # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
     # print(f"Result for writing to /tmp/temp.txt: \n{result}")

     ### run_python_file tests
     result = run_python_file("calculator", "main.py")
     print(f"Result for running 'main.py':\n{result}")

     result = run_python_file("calculator", "main.py", ["3 + 5"])
     print(f"Result for running 'main.py' with arg [\"3 + 5\"]:\n{result}")

     result = run_python_file("calculator", "tests.py")
     print(f"Result for running 'tests.py':\n{result}")

     result = run_python_file("calculator", "../main.py")
     print(f"Result for running '../main.py':\n{result}")

     result = run_python_file("calculator", "nonexistent.py")
     print(f"Result for running 'nonexistent.py':\n{result}")

     result = run_python_file("calculator", "lorem.txt")
     print(f"Result for running 'lorem.txt':\n{result}")

if __name__ == "__main__":
    main()
