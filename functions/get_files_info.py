# get_files_info.py

import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        res_str = ""
        if directory != ".":
            full_dir = os.path.join(working_directory, directory)
            full_dir_abs = os.path.abspath(full_dir)
            if not os.path.isdir(full_dir_abs):
                return f'Error: "{directory}" is not a directory'
            if not full_dir_abs.startswith(os.path.abspath(working_directory)):
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            full_dir_abs = os.path.abspath(working_directory)

        for item in os.listdir(full_dir_abs):
            item_path = os.path.join(full_dir_abs, item)
            item_size = os.path.getsize(item_path)
            item_is_dir = os.path.isdir(item_path)
            res_str += f'- {item}: file_size={item_size}, is_dir={item_is_dir}\n'

        return res_str.rstrip()

    except Exception as e:
        return f'Error: {e}'