# get_file_content.py

import os
import config
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file provided its file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to get content from, relative to the working directory. If not provided, uses current working directory as a file path.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path="."):
    try:
        if file_path != ".":
            full_dir = os.path.join(working_directory, file_path)
            full_dir_abs = os.path.abspath(full_dir)
            if not os.path.isfile(full_dir):
                return f'Error: "{file_path}" does not exist or is not a file'
            if not full_dir_abs.startswith(os.path.abspath(working_directory)):
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            return f'Error: Not a valid file path'

        with open(full_dir_abs, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            if len(file_content_string) >= config.MAX_CHARS:
                file_content_string += f'... File "{file_path}" truncated at 10000 characters'

        return file_content_string

    except Exception as e:
        return f'Error: {e}'
