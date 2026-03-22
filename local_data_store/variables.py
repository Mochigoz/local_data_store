from local_data_store.main import read, append, write
from local_data_store.output import output
import os

from typing import Union

def get_variables_folder() -> str:
    """
    Fetch the folder where all variables are saved or create one if it is not already created
    :return: Path to the folder where all variables of the library are saved
    """
    cache_path: str = os.getenv("LOCALAPPDATA") + "\\local_data_store\\" # Folder where all the variables are saved

    if not os.path.exists(cache_path):
        os.makedirs(cache_path, exist_ok=True)

    return cache_path

def edit_custom_path(name: str, path: str):
    """
    :param name: Name of the variable
    :param path: Assigned path
    :return:
    """

    append(path=get_variables_folder() + r"paths.json", content={name: path})
    output(f"'{name}' value changed to {path}")

# Aliases
new_custom_path = edit_custom_path

def remove_custom_path(name: str):
    """

    :param name: Variable to remove
    :return:
    """

    paths: dict = read(get_variables_folder() + r"paths.json") or {}
    paths.pop(name, None)

    write(get_variables_folder() + r"paths.json", paths)
    output(f"Removed '{name}' variable")

def get_custom_path(name: str) -> Union[str, None]:
    """
    :param name: Name of the variable
    :return: The path assigned to the variable
    """
    paths: dict = read(get_variables_folder() + r"paths.json") or {}
    return paths.get(name)