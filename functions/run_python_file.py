# run_python_file.py

import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file, constrained to the working directory. Run without arguments unless specified",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional arguments to be passed to the file. Leave empty if no arguments were specified.",
            )
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abs_full_path = os.path.abspath(full_path)
        if not abs_full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'
        if not abs_full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'

        run_with_args = f"python3 {abs_full_path} {" ".join(args)}"
        result = subprocess.run(run_with_args, shell=True, cwd=abs_working_dir, capture_output=True, timeout=30)

        res_str = ""
        if ((len(result.stdout) == 0) & (len(result.stderr) == 0)):
                res_str = f'No output produced.'
        else:
            res_str = f'STDOUT:\n{(result.stdout.decode('UTF-8'))}\nSTDERR:\n{result.stderr.decode('UTF-8')}'

        if result.returncode != 0:
            res_str += f'Process exited with code {result.returncode}.'

        return res_str

    except Exception as e:
        return f'Error: executing Python file: {e}'
pass

