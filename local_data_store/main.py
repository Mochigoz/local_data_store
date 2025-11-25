import os
import json
from typing import Union, List, Any

def convert_path(path: str) -> str: # Add .json to the file
    if not path.endswith(r'.json'):
        path += r'.json'

    return path

def read(path: str) -> Union[Any, None]:
    path = convert_path(path)
    if not os.path.exists(path): # Check if path exists
        return None

    try:
        with open(path, 'r') as f: # Try to open the file
            return json.load(f) # Read the file
    except json.JSONDecodeError: # If file corrupted or do not exists return None
        return None

def write(path: str, content: Any):
    """
    Create a new .json file
    :param path: Path to the file
    :param content: Content to be written into the file (must be serializable)
    :return:
    """
    folder_path: str = '\\'.join(path.split('\\')[:-1]) # Get the folder
    if folder_path:
        os.makedirs(folder_path, exist_ok=True)

    path = convert_path(path)
    with open(path, 'w') as f:
        json.dump(
            obj=content,
            fp=f,
            ensure_ascii=False,
            indent=4 # Fancy write
        )

def append(path: str, content: Any) -> Union[List[Any], Any]:
    file_content: Any = read(path)
    if not file_content: # No file
        write(path, content)
        return content

    if isinstance(content, dict) and isinstance(file_content, dict):
        for key, value in content.items():
            file_content[key] = value
    elif not isinstance(file_content, list):
        file_content: list = [file_content]
        file_content.append(content) # Append the value

    path = convert_path(path)
    write(path, file_content) # Write in the file the content
    return file_content # Return the new content

def delete(path: str):
    if not os.path.exists(path):
        return

    os.remove(path)