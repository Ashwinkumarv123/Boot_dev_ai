import json
from collections.abc import Callable

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file
# ... (schemas matrum available_functions eppodhum pola thodara vendum) ...
schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the text contents of a specified file path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The relative file path to read contents from",
                },
            },
            "required": ["file_path"],
        },
    },
}

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes or runs a specified Python script or file with optional command-line arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The relative file path of the Python script or file to execute/run",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional list of command-line arguments to pass to the script",
                },
            },
            "required": ["file_path"],
        },
    },
}

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites text content to a specified file path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The relative file path to write text into",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to be written to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python_file,
    schema_write_file,
]

# Neenga ketta function_map ingu dhaan irukku!
function_map: dict[str, Callable[..., str]] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    
    if verbose:
        print(f" - Calling function: {function_name} ({function_args})")
    else:
        print(f" - Calling function: {function_name}")
        
    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
        
    function_args["working_directory"] = "./calculator"
    result = function_map[function_name](**function_args)
    
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }
